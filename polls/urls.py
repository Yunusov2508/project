from django.urls import path
from .views import AllbookView,DetailBookView,CreateBookView,UpdateBookView,DeleteBookView

urlpatterns =[
    path('',AllbookView.as_view()),
    path('<int:book_id>/',DetailBookView.as_view()),
    path('create/',CreateBookView.as_view()),
    path('update/<int:book_id>/',UpdateBookView.as_view()),
    path('delete/<int:book_id>/',DeleteBookView.as_view()),
]