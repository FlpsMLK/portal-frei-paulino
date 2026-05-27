# 🏫 Portal Frei Paulino

Portal institucional da escola Frei Paulino, desenvolvido com **Python + Django**, conforme especificações do Projeto Integrado Multidisciplinar (PIM).

---

## 📦 Tecnologias Utilizadas

| Tecnologia | Função |
|---|---|
| Python 3.x | Linguagem principal |
| Django 4.x | Framework web (MTV) |
| Django Channels | Chat em tempo real (WebSocket) |
| SQLite / PostgreSQL | Banco de dados relacional |
| Bootstrap 5 | Interface responsiva |

---

## ⚙️ Instalação

### 1. Instalar dependências
```bash
pip install django channels Pillow
```

### 2. Aplicar migrações
```bash
python manage.py migrate
```

### 3. Popular banco com dados de exemplo
```bash
python seed_data.py
```

### 4. Iniciar o servidor
```bash
python manage.py runserver
```

Acesse: **http://127.0.0.1:8000**

---

## 🔐 Credenciais de Acesso (dados de exemplo)

| Usuário | Senha | Tipo |
|---|---|---|
| `admin` | `admin123` | Administrador |
| `prof_ana` | `senha123` | Professora |
| `prof_carlos` | `senha123` | Professor |
| `joao_aluno` | `senha123` | Aluno – Turma 3A |
| `maria_aluno` | `senha123` | Aluno – Turma 3A |
| `pedro_aluno` | `senha123` | Aluno – Turma 2B |

Painel Admin: **http://127.0.0.1:8000/admin**

---

## 🗂️ Módulos do Portal

### 1. 📰 Notícias e Eventos
- Publicação de comunicados, notícias e avisos institucionais
- Filtro por categoria (Geral, Acadêmico, Cultural, Esportivo, Comunicado)
- Calendário de eventos com datas e locais
- Editor de conteúdo com suporte a imagens

### 2. 📝 Blog – Processos Seletivos
- Posts sobre processos seletivos de grandes empresas
- Categorias e tags por empresa/área
- Sistema de busca por título, conteúdo e tags
- Comentários com moderação prévia
- Publicação exclusiva para professores

### 3. 💬 Chat em Tempo Real
- Comunicação via WebSocket (Django Channels)
- Canais públicos (todos podem acessar)
- Canais privados (acesso restrito a membros)
- Histórico de mensagens salvo no banco de dados
- Criação de canais por disciplina (professores)

### 4. 📋 Gestão de Tarefas
- Professores criam tarefas com prazo e critérios
- Alunos fazem upload de respostas em arquivo
- Acompanhamento de entregas em tempo real
- Sistema de notas e feedback individual
- Notificação de prazo expirado

### 5. 👤 Autenticação e Perfis
- Cadastro com perfis diferenciados (aluno/professor/admin)
- Login seguro com senhas criptografadas (PBKDF2+SHA256)
- Controle de acesso por tipo de usuário
- Edição de perfil com foto

---

## 🏛️ Arquitetura

```
portal_frei_paulino/
├── portal/             # Configurações do projeto
│   ├── settings.py
│   ├── urls.py
│   └── asgi.py         # WebSocket (Channels)
├── accounts/           # Autenticação e usuários
├── blog/               # Blog de processos seletivos
├── noticias/           # Notícias, eventos e página inicial
├── chat/               # Chat em tempo real
├── tarefas/            # Gestão de tarefas acadêmicas
├── templates/          # Templates HTML
├── static/             # CSS, JS, imagens
├── seed_data.py        # Script de dados de exemplo
└── manage.py
```

---

## 🚀 Produção (PostgreSQL)

Para usar PostgreSQL em produção, altere em `settings.py`:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'portal_frei_paulino',
        'USER': 'postgres',
        'PASSWORD': 'sua_senha',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

E para o chat em tempo real com Redis:
```python
CHANNEL_LAYERS = {
    'default': {
        'BACKEND': 'channels_redis.core.RedisChannelLayer',
        'CONFIG': {'hosts': [('127.0.0.1', 6379)]},
    },
}
```

---

*Desenvolvido como Projeto Integrado Multidisciplinar – Frei Paulino, Cândido Mota – SP*
