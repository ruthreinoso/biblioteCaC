from django.urls import path
from .views import BookList, BookDetail, BookCreate, BookUpdate, BookDelete, CategoryView


books_patterns = ([
    path('', BookList.as_view(), name='books'),
    path('book/<int:pk>/<slug:slug>/', BookDetail.as_view(), name='book'),
    path('create/', BookCreate.as_view(), name='create'),
    path('update/<int:pk>/', BookUpdate.as_view(), name='update'),
    path('delete/<int:pk>/', BookDelete.as_view(), name='delete'),
    path('category/<int:category_id>/', CategoryView.as_view(), name='category_view')
], 'books' )