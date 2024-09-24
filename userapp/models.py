from django.db import models
from adminapp.models import*

# Create your models here.
class Register(models.Model):
    username=models.TextField()
    password=models.CharField(max_length=100)
    email=models.EmailField(null=True)
    phonenumber=models.IntegerField(default=1234) 

    
class contact1(models.Model):
    name=models.TextField()
    email=models.EmailField(max_length=100)
    message=models.TextField()  
class cart(models.Model):
    cartuser=models.ForeignKey(Register,on_delete=models.CASCADE)
    cartproduct=models.ForeignKey(products,on_delete=models.CASCADE)
    quantity=models.IntegerField()
    total=models.IntegerField()
    status=models.IntegerField(default=0) 
class checkout(models.Model):
    usercheckout=models.ForeignKey(Register,on_delete=models.CASCADE)
    checkoutcart=models.ForeignKey(cart,on_delete=models.CASCADE)
    address=models.CharField(max_length=100)
    city=models.CharField(max_length=100)
    country=models.CharField(max_length=100)
    postcode=models.CharField(max_length=100)

