from django.test import TestCase, Client
from django.urls import reverse
from accounts.models import Usuario

class AutenticacaoTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.professor = Usuario.objects.create_user(
            username='prof_test', password='senha123',
            first_name='Prof', last_name='Teste', tipo='professor'
        )
        self.aluno = Usuario.objects.create_user(
            username='aluno_test', password='senha123',
            first_name='Aluno', last_name='Teste', tipo='aluno', turma='3A'
        )

    def test_login_credenciais_corretas(self):
        response = self.client.post(reverse('login'), {
            'username': 'prof_test', 'password': 'senha123'
        })
        self.assertEqual(response.status_code, 302)

    def test_login_credenciais_erradas(self):
        response = self.client.post(reverse('login'), {
            'username': 'prof_test', 'password': 'errada'
        })
        self.assertEqual(response.status_code, 200)

    def test_cadastro_novo_usuario(self):
        self.client.post(reverse('cadastro'), {
            'username': 'novo_user',
            'first_name': 'Novo', 'last_name': 'Usuario',
            'email': 'novo@teste.com',
            'tipo': 'aluno', 'turma': '2B',
            'password1': 'SenhaSegura@2024',
            'password2': 'SenhaSegura@2024',
        })
        self.assertTrue(Usuario.objects.filter(username='novo_user').exists())

    def test_perfil_requer_login(self):
        response = self.client.get(reverse('perfil'))
        self.assertIn(response.status_code, [301, 302])
        self.assertIn('login', response.url)

    def test_tipo_professor(self):
        self.assertTrue(self.professor.is_professor())
        self.assertFalse(self.aluno.is_professor())

    def test_tipo_aluno(self):
        self.assertTrue(self.aluno.is_aluno())
        self.assertFalse(self.professor.is_aluno())
