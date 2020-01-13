import json
from django.forms.models import model_to_dict
from django.shortcuts import render
from django.http import Http404, JsonResponse, HttpResponseBadRequest
from django.views.generic import ListView

from .models import Book, Comment


# Create your views here.
class BookListView(ListView):
    model = Book


def book_detail_view(request, pk):
    if request.is_ajax():
        return book_detail_view_ajax(request, pk)

    book = Book.objects.get(pk=pk)
    return render(request, template_name="books/book_detail.html", context={
        "book": book
    })


def book_detail_view_ajax(request, pk):
    if request.method == "POST":
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        # Toto je zle, treba validovat data lepsim sposobom.

        user = body.get("user")
        if not user:
            return JsonResponse({'error': 'Request is missing field user.'}, status=500)
        text = body.get("text")
        if not text:
            return JsonResponse({'error': 'Request is missing field text.'}, status=500)
        book = body.get("book")
        if not book:
            return JsonResponse({'error': 'Request is missing field book.'}, status=500)

        comment = Comment(book_id=book, text=text, user=user)
        comment.save()
        return JsonResponse(model_to_dict(comment), safe=False)

    else:
        pass
