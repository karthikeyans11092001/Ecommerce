from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    email = models.EmailField(null=True)
    date_of_birth = models.DateField(blank=True,null=True)
    address = models.CharField(max_length=255)
    contact = models.CharField(max_length=20)
    def __str__(self):
        return self.username

class Products(models.Model):
    product_id=models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=255)
    price = models.DecimalField(decimal_places=2, max_digits=8)
    image = models.ImageField(upload_to='members/images/')
    def __str__(self):
        return self.name
class Order(models.Model):
    order_id=models.AutoField(primary_key=True)
    customer = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    products = models.ManyToManyField(Products, through='OrderItem')
    def __str__(self):
        return str(self.order_id)

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

