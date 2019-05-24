from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
class EMP(models.Model):
    sno=models.IntegerField()
    sname=models.CharField(max_length=20)
    sal=models.IntegerField()

    def __str__(self): #String Represention
        return self.sname
