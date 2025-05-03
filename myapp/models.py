from mongoengine import Document, StringField, ListField

class Event(Document):
    title = StringField(required=True)
    event = ListField(StringField())