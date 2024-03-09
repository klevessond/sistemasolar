from django.urls import path
from usinas.views import usinas, cadastro_painelsolar, cadastro_inversor, cadastro_usina


urlpatterns = [
    path('usinas/', usinas, name='usinas'),
    path('cadastro_painelsolar/', cadastro_painelsolar, name='cadastro_painelsolar'),
    path('cadastro_inversor/', cadastro_inversor, name='cadastro_inversor'),
    path('cadastro_usina/', cadastro_usina, name='cadastro_usina'),
        
]
