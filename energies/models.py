from django.db import models

# Create your models here.
from mongoengine import Document, fields

class Energy(Document):
    title = fields.StringField(required=True)
    code = fields.StringField(required=True)
    year = fields.IntField(required=True)
    inventors = fields.StringField(required=True)
    num_inventors = fields.IntField(required=True)
    abstract = fields.StringField(required=True)