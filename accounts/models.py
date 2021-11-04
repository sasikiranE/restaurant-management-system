from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    mobile_number = models.CharField(max_length=12)
    city = models.CharField(max_length=200)
    pincode = models.IntegerField()
    address = models.CharField(max_length=300)

    def __str__(self):
        return self.user.username