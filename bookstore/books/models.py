from django.db import models


# Create your models here.
class Book(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=500)

    def __str__(self):
        return self.name


class Comment(models.Model):
    user = models.CharField(max_length=40, null=True)
    text = models.TextField(max_length=400)
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='comments')

    def __str__(self):
        return "Comment from %s for a book %s" % (self.user, self.book)
