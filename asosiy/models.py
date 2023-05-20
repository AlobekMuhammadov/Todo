from django.db import models

class Reja(models.Model):
    sarlavha = models.CharField(max_length=20)
    sana = models.DateField(auto_now_add=True)
    batafsil = models.TextField()
    yonalish = models.CharField(max_length=100, choices=[('Hozirgi maqsad','Hozirgi maqsad'),('Kelajakdagi maqsad','Kelajakdagi maqsad')], null=True, blank=True)
    def __str__(self):
        return f"{self.sarlavha}"
