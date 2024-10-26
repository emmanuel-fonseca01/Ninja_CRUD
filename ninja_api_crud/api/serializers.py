from ninja import schema
from datetime import date


class BookSchema(schema):
    title: str
    author: str
    publication_year: date
