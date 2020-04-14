from django.db import models


class RegistroHoraExtra(models.Model):
    motivo = models.CharField(max_length=100, help_text="motivo para realizacao da hora extra")

    def __str__(self):
        return self.motivo
