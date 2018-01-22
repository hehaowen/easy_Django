from django.db import models

# Create your models here.
class Author(models.Model):
    aut_name = models.CharField(max_length=20,verbose_name='姓名')
    hometown = models.CharField(max_length=100,verbose_name='家乡')
    def __str__(self):
        return self.aut_name