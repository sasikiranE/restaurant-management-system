from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Item(models.Model):

    category_choices = (
        ('chicken', 'chicken'),
        ('drinks', 'drinks'),
        ('steak', 'steak'),
        ('pizzas', 'pizzas'),
        ('burgers', 'burgers'),
        ('sandwich', 'sandwich'),
        ('nuggets', 'nuggets'),
        ('other', 'other'),
    )

    name = models.CharField(max_length=200)
    price = models.IntegerField()
    photo = models.ImageField(upload_to='media/fooditems/%Y/%m')
    category = models.CharField(choices=category_choices, max_length=200)
    description = models.TextField()
    is_veg = models.BooleanField(default=True)
    is_featured = models.BooleanField(default=False)
    is_available = models.BooleanField(default=True)
    limit = models.IntegerField(default=3)
    last_modified = models.DateTimeField(auto_now=True)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    food = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username
