from ninja import Schema
from datetime import date

class PostSchema(Schema):
    title: str
    text: str
    author_id: int
    category_id: int
    publish_date: date
    status: bool
