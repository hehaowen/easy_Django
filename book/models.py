from django.db import models
from author.models import Author
from publisher.models import Publisher
# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=32,verbose_name='书名')
    authors = models.ManyToManyField(Author)
    publishers = models.ForeignKey(Publisher,verbose_name='出版社')
    def __str__(self):
        return self.title

