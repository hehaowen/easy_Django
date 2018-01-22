from django.shortcuts import render
from book.models import Book
# Create your views here.
def Book_def(request):
    Book_all = Book.objects.all()
    return render(request,'index.html',{'Boo':Book_all})

def detail(request, id):
    book_detail = Book.objects.get(id=id)
    return render(request, 'book/detail.html', {'book_detail':book_detail})

def book_book(request):
    book_books = Book.objects.all()
    return render(request,'book/book.html',{'book_books':book_books})