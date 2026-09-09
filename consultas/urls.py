from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_consultas, name='home_consulta'),
    path('cadastrar/', views.cadastrar, name='cadastrar'),
    path('editar/', views.editar, name='editar'),
]
