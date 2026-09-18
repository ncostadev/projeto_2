from django.db import models

# Create your models here.

class Consulta(models.Model):
    paciente = models.CharField(max_length=100)
    medico = models.CharField(max_length=100)
    especialidade = models.CharField(max_length=100)
    data = models.DateField()
    horario = models.TimeField()
    status = models.CharField(max_length=20)

    def __str__(self):
        return f"Consulta de {self.paciente} com {self.medico} em {self.data} às {self.horario}"
    
