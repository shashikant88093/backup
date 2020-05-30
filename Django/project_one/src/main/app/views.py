from django.shortcuts import render
from django.http import HttpResponse
from .models import Book,Table
from django.views import View
from rest_framework import viewsets
from .serializers import BookSerializer, TableSerializer
from rest_framework.authentication import TokenAuthentication
# Create your views here.
# class Another(View):
#     # books = Book.objects.filter(is_published=True)
#     books = Book.objects.get(id=1)
#     output = f"We have id {books.id}  in DB<br>"
#
#     # for book in books:
#         # output += f"We have {book.title} book,
#         id {book.id},
#         price {book.price} in DB<br>"
#     def get(self,request):
#         return HttpResponse(self.output)
#
# class Tables(View):
#     tables = Table.objects.all()
#     def get(self,request):
#         return HttpResponse(self.tables)

# def first(request):
#     books = Book.objects.all()
#     return render(request,'first_temp.html',
#                   {'books':books})

class BookViewSet(viewsets.ModelViewSet):
    serializer_class = BookSerializer
    queryset = Book.objects.all()
    authentication_classes = (TokenAuthentication,)



class TableViewSet(viewsets.ModelViewSet):
    serializer_class = TableSerializer
    queryset = Table.objects.all()
    authentication_classes = (TokenAuthentication,)


