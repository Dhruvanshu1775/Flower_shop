from django.db import models

# Create your models here.


class user_details(models.Model):
    username = models.CharField(max_length=20)
    email = models.EmailField()
    password = models.CharField(max_length=20)

    def __str__(self):
        return self.username


class flower_product(models.Model):
    image = models.ImageField()
    name = models.CharField(max_length=50)
    bouquet_type = models.CharField(max_length=20)
    price = models.IntegerField()
    description = models.TextField()

    def __str__(self):
        return self.name
