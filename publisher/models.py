from django.db import models

# Create your models here.
class Publisher(models.Model):
    Pub_name = models.CharField(max_length=32,verbose_name='出版社')
    address = models.CharField(max_length=100,verbose_name='地址')
    website = models.CharField(max_length=32,verbose_name='网站')
    def __str__(self):
        return self.Pub_name