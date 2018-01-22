from django.shortcuts import render
from author.models import Author
# Create your views here.
def Author_def(request):
    Author_all = Author.objects.all()
    return render(request,'index.html',{'Aut':Author_all})

def detail(request, id):
    Author_detail = Author.objects.get(id=id)
    return render(request,'author/detail.html',{'Author_detail':Author_detail})

def Authors(request):
    authorsr = Author.objects.all()
    return render(request,'author/authors.html',{'authorsr':authorsr})