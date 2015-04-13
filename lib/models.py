from mongoengine import Document, StringField, DateTimeField, FloatField


class Price(Document):
    product_name = StringField(max_length=200)
    time = DateTimeField()
    price = FloatField()