from rest_framework import serializers
from .models import AuthorModel,BookCategoryModel,BookModel




class AuthirSerializer(serializers.ModelSerializer):
    class Meta:
        model = AuthorModel
        fields = ('name','fname','date_of_birth','counrty')


class BookCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = BookCategoryModel
        fields = ('name',)



class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookModel
        fields = ('author','name','category','page','price')