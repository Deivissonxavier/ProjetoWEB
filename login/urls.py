from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect

urlpatterns = [
    # Redirecionamento para a página de login caso a URL raiz seja acessada
    path('', lambda request: redirect('login')),  # Redireciona para a página de login
    
    # Admin e outras URLs da aplicação
    path('admin/', admin.site.urls),
    path('login/', include('app_login.urls')),  # Redireciona para o app_login
    path('register/', include('app_create_account.urls')),
    path('change/', include('app_change_account.urls')), # Modificado para o formulário
    path('welcome/', include('app_welcome.urls')),
    path('administrator/', include('app_admin.urls')),
]
