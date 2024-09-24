from django.db import models


# Create your models here.
class catagories(models.Model):
    name=models.TextField()
    image=models.ImageField(upload_to="image",default="null.jpg")
class products(models.Model):
    name=models.TextField()
    image=models.ImageField(upload_to="image",default="null.jpg")
    price=models.IntegerField()
    category=models.TextField()
    features=models.TextField()     