from django.shortcuts import render,get_object_or_404
from rest_framework.views import APIView
from .models import BookModel
from rest_framework.response import Response
from .serializers import BookSerializer
from rest_framework import status

class AllbookView(APIView):
    def get(self,request,*args,**kwargs):
        all_book = BookModel.objects.all()
        serializer = BookSerializer(all_book,many=True)
        return Response(serializer.data)

class DetailBookView(APIView):
    def get(self,request,*args,**kwargs):
        book = get_object_or_404(BookModel,pk='')
        serializer = BookSerializer(book)
        return Response(serializer.data)
    
class CreateBookView(APIView):
    def post(self,request,*args,**kwargs):
        serializer = BookSerializer(data=request)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    

class UpdateBookView(APIView):
    def patch(self,request,*args,**kwargs):
        instance = get_object_or_404(BookModel,pk=kwargs['book_id'])
        serializer = BookSerializer(instance,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    
class DeleteBookView(APIView):
    def delete(self,request,*args,**kwargs):
        instance = get_object_or_404(BookModel,pk=kwargs['book_id'])
        instance.delete()
        return Response({'delete':'success'},status=status.HTTP_204_NO_CONTENT) 