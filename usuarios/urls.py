from django.urls import path
from usuarios.views import index

urlpatterns = [
        path('', index, name='index')
]
