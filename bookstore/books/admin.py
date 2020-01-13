from django.contrib import admin
from .models import Comment, Book
# Register your models here.

admin.site.register(Comment)
admin.site.register(Book)