from django.contrib import admin
from .models import BookCategoryModel,BookModel,AuthorModel
# Register your models here.

admin.site.register(BookCategoryModel)
admin.site.register(BookModel)
admin.site.register(AuthorModel)
