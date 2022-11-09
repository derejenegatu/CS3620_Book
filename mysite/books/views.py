from django.shortcuts import render
from.models import Book
from django.core.paginator import Paginator
# Create your views here.


def book_list(request):
    book_object = Book.objects.all()
    book_Name = request.GET.get('book_Name')
    if book_Name != '' and book_Name is not None:
        book_object = book_object.filter(Name__icontains=book_Name)
    paginator = Paginator(book_object, 6)
    page = request.GET.get('page')
    book_object = paginator.get_page(page)
    return render(request, 'books/book_list.html', {'book_object': book_object})
