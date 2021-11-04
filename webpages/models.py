from django.db import models

# Create your models here.
class Slider(models.Model):
    headline = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=200)
    button_text = models.CharField(max_length=200)
    photo = models.ImageField(upload_to='media/sliders/')
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.headline


class Team(models.Model):
    name = models.CharField(max_length=200)
    role = models.CharField(max_length=200)
    photo = models.ImageField(upload_to='media/team/')
    fb_link = models.CharField(max_length=200)
    insta_link = models.CharField(max_length=200)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Contact(models.Model):
    firstname = models.CharField(max_length=200)
    lastname = models.CharField(max_length=200)
    phone_number = models.IntegerField()
    email = models.CharField(max_length=200)
    subject = models.CharField(max_length=200)
    details_message = models.TextField()

    def __str__(self):
        return self.subject
