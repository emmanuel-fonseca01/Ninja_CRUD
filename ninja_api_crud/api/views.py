from ninja import NinjaAPI
from .models import Book
from .serializers import BookSchema, BookSchemaOut
from typing import List
from django.shortcuts import get_object_or_404

api = NinjaAPI()

@api.post("/books")
def create_book(request, payload: BookSchema):
    book = Book.objects.create(**payload.dict())
    return {"id": book.id}


@api.get("/books/{book_id}", response=BookSchemaOut)
def get_book(request, book_id: int):
    book = get_object_or_404(Book, id=book_id)
    return book


@api.get("/books", response=List[BookSchemaOut])
def list_books(request):
    qs = Book.objects.all()
    return qs

@api.put("/books/{book_id}")
def update_book(request, book_id: int, payload: BookSchema):
    book = get_object_or_404(Book, id=book_id)
    for attr, value in payload.dict().items():
        setattr(book, attr, value)
    book.save()
    return {"message: success"}
