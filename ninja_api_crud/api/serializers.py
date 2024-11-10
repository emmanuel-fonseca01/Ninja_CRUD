from ninja import Schema
from datetime import date


class BookSchema(Schema):
    title: str
    author: str
    publication_date: date

class BookSchemaOut(Schema):
    id: int
    title: str
    author: str
    publication_date: date