from django.contrib import admin
from .models import Products,CustomUser
# Register your models here.
admin.site.register(CustomUser)
admin.site.register(Products)