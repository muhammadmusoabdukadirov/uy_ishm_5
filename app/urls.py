from django.urls import path, include
from .views import index, book_detail, author_detail

urlpatterns = [
    path('', index, name='index'),
    path('book/<int:pk>/', book_detail, name='book_detail'),
    path('author/<int:pk>/', author_detail, name='author_detail')

]