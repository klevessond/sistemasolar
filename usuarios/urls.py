from django.urls import path
from usuarios.views import index,login,cadastro,logout,listar_usuarios,detalhar_usuarios,cadastrar_usuarios


urlpatterns = [
    path('index/', index, name='index'),
    path('login/', login, name='login'),
    path('cadastro/', cadastro, name='cadastro'),
    path('logout', logout, name='logout'),
    path('listar_usuarios/', listar_usuarios, name='listar_usuarios'),
    path('detalhar_usuarios/<int:user_id>/', detalhar_usuarios, name='detalhar_usuarios'),
    path('cadastrar_usuarios/', cadastrar_usuarios, name='cadastrar_usuarios'),


]
