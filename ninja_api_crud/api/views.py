from ninja import NinjaAPI
from .models import Book
from .serializers import BookSchema

api = NinjaAPI()

@api.post("/books")
def create_book(request, payload: BookSchema):
    book = Book.objects.create(**payload.dict())
    return {"id": book.id}