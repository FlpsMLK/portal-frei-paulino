from django.test import TestCase, Client
from django.urls import reverse
from accounts.models import Usuario
from blog.models import Post, Categoria

class BlogTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.professor = Usuario.objects.create_user(
            username='prof_blog', password='senha123', tipo='professor'
        )
        self.aluno = Usuario.objects.create_user(
            username='aluno_blog', password='senha123', tipo='aluno', turma='3A'
        )
        self.cat = Categoria.objects.create(nome='Tech', slug='tech')
        self.post = Post.objects.create(
            titulo='Post de Teste', slug='post-de-teste',
            autor=self.professor, conteudo='Conteúdo de teste completo aqui.',
            status='publicado', categoria=self.cat
        )

    def test_lista_posts_publica(self):
        response = self.client.get(reverse('lista_posts'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Post de Teste')

    def test_detalhe_post_publicado(self):
        response = self.client.get(reverse('detalhe_post', args=['post-de-teste']))
        self.assertEqual(response.status_code, 200)

    def test_criar_post_requer_professor(self):
        self.client.login(username='aluno_blog', password='senha123')
        response = self.client.get(reverse('criar_post'))
        self.assertEqual(response.status_code, 302)

    def test_professor_pode_criar_post(self):
        self.client.login(username='prof_blog', password='senha123')
        response = self.client.get(reverse('criar_post'))
        self.assertEqual(response.status_code, 200)

    def test_busca_posts(self):
        response = self.client.get(reverse('busca_posts') + '?q=Teste')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Post de Teste')

    def test_busca_sem_resultado(self):
        response = self.client.get(reverse('busca_posts') + '?q=xyzabcnaoexiste')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, '0 resultado')
