from django.db import models

# Create your models here.
class Member(models.Model):
    name = models.CharField(max_length=200)
    phone = models.CharField(default="+880", max_length=14)
    date_time_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    date_time_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    