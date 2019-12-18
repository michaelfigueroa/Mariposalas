from django.db import models

# Create your models here.
class PanPascua(models.Model):
    #id=models.AutoField(primary_key=True)
    nombre=models.CharField(max_length=30)
    peso=models.DecimalField(max_digits=2, decimal_places=1)
    valor=models.IntegerField()
    image=models.ImageField(upload_to="photos")
    descripcion=models.TextField()

    def alta(self):
        self.save()

    def __str__(self):
        return self.nombre
