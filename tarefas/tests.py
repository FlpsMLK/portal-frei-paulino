from django.test import TestCase, Client
from django.urls import reverse
from django.utils import timezone
from datetime import timedelta
from accounts.models import Usuario
from tarefas.models import Tarefa

class TarefasTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.professor = Usuario.objects.create_user(
            username='prof_tar', password='senha123', tipo='professor'
        )
        self.aluno = Usuario.objects.create_user(
            username='aluno_tar', password='senha123', tipo='aluno', turma='3A'
        )
        self.tarefa = Tarefa.objects.create(
            titulo='Tarefa Teste',
            descricao='Descrição da tarefa de teste.',
            professor=self.professor, turma='3A',
            prazo=timezone.now() + timedelta(days=7),
            status='aberta'
        )

    def test_lista_tarefas_requer_login(self):
        response = self.client.get(reverse('lista_tarefas'))
        self.assertIn(response.status_code, [301, 302])

    def test_aluno_ve_tarefa_da_sua_turma(self):
        self.client.login(username='aluno_tar', password='senha123')
        response = self.client.get(reverse('lista_tarefas'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Tarefa Teste')

    def test_professor_ve_suas_tarefas(self):
        self.client.login(username='prof_tar', password='senha123')
        response = self.client.get(reverse('lista_tarefas'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Tarefa Teste')

    def test_prazo_nao_expirado(self):
        self.assertFalse(self.tarefa.prazo_expirado())

    def test_prazo_expirado(self):
        self.tarefa.prazo = timezone.now() - timedelta(days=1)
        self.tarefa.save()
        self.assertTrue(self.tarefa.prazo_expirado())

    def test_aluno_nao_pode_criar_tarefa(self):
        self.client.login(username='aluno_tar', password='senha123')
        response = self.client.get(reverse('criar_tarefa'))
        self.assertEqual(response.status_code, 302)
