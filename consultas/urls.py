from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_consultas, name='home_consulta'),
    path('cadastrar/', views.cadastrar, name='cadastrar'),
    path('editar/<int:id>/', views.editar, name='editar'),
]
