from django.shortcuts import render

# Create your views here.
from django.http import HttpRequest, HttpResponse
from .models import Genre, Book, Author

def index(request):
    query = request.GET.get('q', '')
    janr_id = request.GET.get('janr', None)

    kitoblar = Book.objects.all()
    if query:
        kitoblar = kitoblar.filter(name__icontains=query)
    if janr_id:
        kitoblar = kitoblar.filter(genre_id=janr_id)

    janrlar = Genre.objects.all()
    context = {
        "janrlar": janrlar,
        "kitoblar": kitoblar,
        'q': query
    }
    return render(request, "app/index.html", context)


from django.shortcuts import get_object_or_404

def book_detail(request, pk):
    kitob = get_object_or_404(Book, pk=pk)
    return render(request, "app/book_detail.html", {"kitob": kitob})


def author_detail(request, pk):
    author = get_object_or_404(Author, pk=pk)
    return render(request, "app/author_detail.html", {"author": author})
