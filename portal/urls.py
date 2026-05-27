from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('blog/', include('blog.urls')),
    path('noticias/', include('noticias.urls')),
    path('chat/', include('chat.urls')),
    path('tarefas/', include('tarefas.urls')),
    path('', include('noticias.urls_home')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
