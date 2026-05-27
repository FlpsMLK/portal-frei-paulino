"""
Script para popular o banco com dados de exemplo.
Execute: python seed_data.py
"""
import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'portal.settings')
django.setup()

from django.utils import timezone
from datetime import timedelta
from accounts.models import Usuario
from blog.models import Post, Categoria, Comentario
from noticias.models import Noticia, Evento
from chat.models import Canal, Mensagem
from tarefas.models import Tarefa

print("🌱 Criando dados de exemplo...")

# ── USUÁRIOS ──────────────────────────────────────────
admin = Usuario.objects.create_superuser(
    username='admin', password='admin123',
    email='admin@freipaulino.edu.br',
    first_name='Administrador', last_name='Portal',
    tipo='admin'
)

prof1 = Usuario.objects.create_user(
    username='prof_ana', password='senha123',
    email='ana@freipaulino.edu.br',
    first_name='Ana', last_name='Souza',
    tipo='professor', turma=''
)

prof2 = Usuario.objects.create_user(
    username='prof_carlos', password='senha123',
    email='carlos@freipaulino.edu.br',
    first_name='Carlos', last_name='Ferreira',
    tipo='professor'
)

aluno1 = Usuario.objects.create_user(
    username='joao_aluno', password='senha123',
    email='joao@aluno.freipaulino.edu.br',
    first_name='João', last_name='Oliveira',
    tipo='aluno', turma='3A'
)

aluno2 = Usuario.objects.create_user(
    username='maria_aluno', password='senha123',
    email='maria@aluno.freipaulino.edu.br',
    first_name='Maria', last_name='Lima',
    tipo='aluno', turma='3A'
)

aluno3 = Usuario.objects.create_user(
    username='pedro_aluno', password='senha123',
    email='pedro@aluno.freipaulino.edu.br',
    first_name='Pedro', last_name='Costa',
    tipo='aluno', turma='2B'
)

print("✅ Usuários criados")

# ── NOTÍCIAS ──────────────────────────────────────────
Noticia.objects.create(
    titulo='Bem-vindos ao Novo Portal Institucional!',
    conteudo='''A escola Frei Paulino lança oficialmente seu portal institucional digital, desenvolvido com tecnologia moderna para aproximar alunos, professores e a gestão escolar.\n\nO portal conta com módulos de notícias, blog de processos seletivos, chat em tempo real e gestão de tarefas acadêmicas.\n\nAcesse todas as funcionalidades fazendo login com sua conta institucional.''',
    autor=admin, categoria='comunicado', destaque=True
)

Noticia.objects.create(
    titulo='Semana de Preparação para o Mercado de Trabalho',
    conteudo='''Durante a próxima semana, a escola Frei Paulino realizará uma série de palestras e workshops voltados à preparação dos alunos para o mercado de trabalho.\n\nProfissionais de empresas como Google, Magazine Luiza, Ambev e Embraer participarão com depoimentos e dicas valiosas sobre processos seletivos.\n\nAs atividades serão realizadas no auditório principal, das 14h às 17h.''',
    autor=prof1, categoria='academico', destaque=True
)

Noticia.objects.create(
    titulo='Calendário de Provas – 2º Semestre 2024',
    conteudo='''Confira abaixo as datas das provas do segundo semestre letivo de 2024.\n\nAgosto: Avaliações parciais de todas as disciplinas\nSetembro: Provas bimestrais\nOutubro: Provas de recuperação parcial\nNovembro: Avaliações finais\nDezembro: Provas de recuperação final\n\nConsulte seu professor em caso de dúvidas.''',
    autor=admin, categoria='academico', destaque=False
)

Noticia.objects.create(
    titulo='Festival Cultural 2024 – Inscrições Abertas',
    conteudo='''As inscrições para o Festival Cultural 2024 estão abertas! Alunos interessados em participar com apresentações de música, dança, teatro ou artes visuais devem se inscrever até o dia 30 deste mês.\n\nO festival acontecerá no dia 15 de novembro, no ginásio da escola.''',
    autor=prof2, categoria='cultural', destaque=False
)

print("✅ Notícias criadas")

# ── EVENTOS ──────────────────────────────────────────
now = timezone.now()
Evento.objects.create(
    titulo='Palestra: Como é trabalhar na Google?',
    descricao='Engenheiro de Software sênior da Google Brasil compartilha sua trajetória e dicas para o processo seletivo da empresa.',
    data_inicio=now + timedelta(days=5, hours=14),
    data_fim=now + timedelta(days=5, hours=16),
    local='Auditório Principal',
    categoria='academico',
    criado_por=prof1
)

Evento.objects.create(
    titulo='Workshop: Currículo e LinkedIn',
    descricao='Aprenda a construir um currículo atraente e otimize seu perfil no LinkedIn para se destacar nos processos seletivos.',
    data_inicio=now + timedelta(days=8, hours=9),
    data_fim=now + timedelta(days=8, hours=12),
    local='Sala de Informática',
    categoria='academico',
    criado_por=prof2
)

Evento.objects.create(
    titulo='Festival Cultural 2024',
    descricao='Grande apresentação dos talentos culturais da escola: música, dança, teatro e artes visuais.',
    data_inicio=now + timedelta(days=45, hours=14),
    local='Ginásio da Escola',
    categoria='cultural',
    criado_por=admin
)

Evento.objects.create(
    titulo='Campeonato Interno de Futsal',
    descricao='Torneio interno entre as turmas. Inscrições encerradas. Confira o bracket na secretaria.',
    data_inicio=now + timedelta(days=12, hours=8),
    data_fim=now + timedelta(days=12, hours=18),
    local='Quadra Esportiva',
    categoria='esportivo',
    criado_por=admin
)

print("✅ Eventos criados")

# ── BLOG ──────────────────────────────────────────────
cat_tech, _ = Categoria.objects.get_or_create(nome='Tecnologia', slug='tecnologia')
cat_negocios, _ = Categoria.objects.get_or_create(nome='Negócios', slug='negocios')
cat_dicas, _ = Categoria.objects.get_or_create(nome='Dicas Gerais', slug='dicas-gerais')

post1 = Post.objects.create(
    titulo='Como é o processo seletivo da Google Brasil?',
    subtitulo='Guia completo com todas as etapas, dicas e o que esperar de cada fase da seleção',
    slug='processo-seletivo-google-brasil',
    autor=prof1, categoria=cat_tech,
    empresa='Google',
    tags='google, tech, engenharia, entrevista técnica, algoritmos',
    conteudo='''O processo seletivo da Google é considerado um dos mais rigorosos do mundo — mas com a preparação certa, é totalmente possível passar por todas as etapas. Neste post, compartilhamos tudo o que você precisa saber.

ETAPA 1 — TRIAGEM DE CURRÍCULO
A Google recebe milhares de candidaturas por semana. Seu currículo precisa ser objetivo e destacar projetos reais que você realizou. Evite clichês como "trabalho bem em equipe" sem exemplos concretos.

ETAPA 2 — ENTREVISTA DE PHONE SCREEN
Uma ligação de 45 minutos com um recrutador, cobrindo experiências passadas, motivação e fit cultural. Prepare respostas usando o método STAR (Situação, Tarefa, Ação, Resultado).

ETAPA 3 — ENTREVISTAS TÉCNICAS (ONSITE OU VIRTUAL)
São geralmente 4 a 5 entrevistas de 45 minutos cada, focadas em:
- Estruturas de dados e algoritmos (essencial!)
- Design de sistemas
- Comportamento e liderança

DICAS DE OURO:
→ Pratique LeetCode diariamente por pelo menos 3 meses antes
→ Estude Big O notation com profundidade
→ Treine em voz alta — explique seu raciocínio enquanto codifica
→ Conheça bem os valores da Google (Googleyness)

BOA SORTE! A preparação consistente faz toda a diferença.''',
    status='publicado'
)

post2 = Post.objects.create(
    titulo='Processo Seletivo Magazine Luiza: do trainee ao efetivo',
    subtitulo='Tudo sobre o programa de trainee e as etapas para entrar em uma das maiores varejistas do Brasil',
    slug='processo-seletivo-magazine-luiza',
    autor=prof2, categoria=cat_negocios,
    empresa='Magazine Luiza',
    tags='magalu, varejo, trainee, gestão, liderança',
    conteudo='''O Magazine Luiza é um dos maiores empregadores do Brasil e tem um dos programas de trainee mais concorridos do setor de varejo. Confira como funciona a seleção.

PROGRAMA DE TRAINEE MAGALU
O programa dura 18 meses e pode levar o trainee a assumir uma gerência de loja ao final. É intenso, prático e transforma jovens profissionais em líderes.

ETAPAS DO PROCESSO:
1. Inscrição online com vídeo de apresentação
2. Testes online de raciocínio lógico e inglês
3. Dinâmica de grupo virtual
4. Entrevista individual com RH
5. Painel com diretores

O QUE A MAGALU VALORIZA:
- Vontade genuína de aprender
- Orientação a resultado
- Liderança pelo exemplo
- Diversidade e inclusão são pilares da empresa

DICA ESPECIAL: A Magalu valoriza muito candidatos que conhecem a empresa a fundo. Pesquise sobre Luiza Helena Trajano, a história da empresa e os valores do "Jeito Magalu de ser".''',
    status='publicado'
)

post3 = Post.objects.create(
    titulo='5 erros que eliminam candidatos logo na triagem de currículo',
    subtitulo='Evite esses erros comuns e aumente suas chances de ser chamado para a entrevista',
    slug='erros-triagem-curriculo',
    autor=prof1, categoria=cat_dicas,
    empresa='',
    tags='currículo, dicas, triagem, RH, processo seletivo',
    conteudo='''A maioria dos candidatos é eliminada antes mesmo de falar com um recrutador. Veja os erros mais comuns e como corrigi-los.

ERRO 1: Currículo com mais de 2 páginas
Recrutadores gastam em média 7 segundos por currículo. Seja objetivo. Se você tem menos de 5 anos de experiência, 1 página é suficiente.

ERRO 2: Objetivo genérico
"Busco oportunidade de crescimento profissional" não diz nada. Substitua por um resumo de 2 linhas que destaque sua especialidade e o que você oferece.

ERRO 3: Listar responsabilidades em vez de conquistas
Errado: "Responsável pelo atendimento ao cliente"
Certo: "Reduzi o tempo médio de atendimento em 30%, elevando o NPS da loja de 72 para 89"

ERRO 4: Foto inadequada ou ausência de foto (quando esperada)
Em empresas brasileiras, foto profissional ainda é comum. Use fundo neutro e traje adequado.

ERRO 5: Erros de português
Um único erro de português pode ser suficiente para eliminar um candidato. Revise, peça para alguém revisar e revise de novo.''',
    status='publicado'
)

# Comentário aprovado no post1
Comentario.objects.create(
    post=post1, autor=aluno1,
    conteudo='Excelente post professora Ana! Já comecei a estudar pelo LeetCode. Tem algum material sobre sistemas distribuídos para a fase de design?',
    aprovado=True
)

print("✅ Blog criado")

# ── CHAT ──────────────────────────────────────────────
canal_geral = Canal.objects.create(
    nome='Geral', descricao='Canal aberto para todos os alunos e professores',
    tipo='publico', criado_por=admin
)
canal_geral.membros.add(admin, prof1, prof2, aluno1, aluno2, aluno3)

canal_3a = Canal.objects.create(
    nome='Turma 3A', descricao='Canal exclusivo da turma 3A — dúvidas e recados',
    tipo='publico', criado_por=prof1
)
canal_3a.membros.add(prof1, aluno1, aluno2)

# Mensagens de exemplo
Mensagem.objects.create(canal=canal_geral, remetente=admin,
    conteudo='Bem-vindos ao Portal Frei Paulino! 🎉 Este é o canal geral da escola.')
Mensagem.objects.create(canal=canal_geral, remetente=prof1,
    conteudo='Oi pessoal! Qualquer dúvida sobre processos seletivos pode perguntar aqui.')
Mensagem.objects.create(canal=canal_geral, remetente=aluno1,
    conteudo='Professora, vai ter simulado de entrevista essa semana?')
Mensagem.objects.create(canal=canal_3a, remetente=prof1,
    conteudo='Turma 3A, não esqueçam: prazo da tarefa de Algoritmos é sexta-feira!')
Mensagem.objects.create(canal=canal_3a, remetente=aluno2,
    conteudo='Professora, posso entregar em PDF?')

print("✅ Chat criado")

# ── TAREFAS ──────────────────────────────────────────
tarefa1 = Tarefa.objects.create(
    titulo='Algoritmos de Busca – Implementação e Análise',
    descricao='''Implemente em Python os algoritmos de busca abaixo e analise a complexidade de cada um:\n\n1. Busca Linear\n2. Busca Binária\n3. Busca em Árvore Binária de Busca (BST)\n\nPara cada algoritmo:\n- Escreva o código comentado\n- Apresente a complexidade de tempo e espaço no Big O\n- Crie um gráfico comparando a performance com listas de 100, 1000 e 10000 elementos\n\nEnvie um único arquivo .py ou .pdf com código e análise.''',
    professor=prof1, turma='3A',
    prazo=timezone.now() + timedelta(days=7),
    criterios='Código correto e comentado (40%), Análise de complexidade (30%), Gráfico comparativo (30%)',
    status='aberta'
)

tarefa2 = Tarefa.objects.create(
    titulo='Pesquisa: Sistemas de Informação na Educação',
    descricao='''Faça uma pesquisa sobre como os Sistemas de Informação estão transformando a educação no Brasil.\n\nO trabalho deve conter:\n- Introdução (mínimo 1 página)\n- 3 exemplos de SI utilizados em escolas ou universidades brasileiras\n- Vantagens e desafios da adoção de SI no ambiente escolar\n- Conclusão\n- Referências bibliográficas (mínimo 3 fontes)\n\nFormato: PDF, fonte Times New Roman 12, espaçamento 1,5, mínimo 5 páginas.''',
    professor=prof2, turma='todas',
    prazo=timezone.now() + timedelta(days=14),
    criterios='Conteúdo e pesquisa (50%), Formatação (20%), Argumentação e conclusão (30%)',
    status='aberta'
)

print("✅ Tarefas criadas")

print("\n" + "="*50)
print("✨ Dados de exemplo criados com sucesso!")
print("="*50)
print("\n📋 CREDENCIAIS DE ACESSO:")
print("  Admin:      admin / admin123")
print("  Professor:  prof_ana / senha123")
print("  Professor:  prof_carlos / senha123")
print("  Aluno:      joao_aluno / senha123  (Turma 3A)")
print("  Aluno:      maria_aluno / senha123 (Turma 3A)")
print("  Aluno:      pedro_aluno / senha123 (Turma 2B)")
print("\n🚀 Para iniciar: python manage.py runserver")
