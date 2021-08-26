from django.db import models


class Register(models.Model):
    username = models.CharField(max_length=50),
    email = models.CharField(max_length=50),
    password = models.CharField(max_length=40)

    def __str__(self):
        return self.username


class Product(models.Model):
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    price = models.IntegerField()
    stock = models.IntegerField()
    imageUrl = models.URLField()
    status = models.BooleanField()
    date_added = models.DateField()
    created = models.ForeignKey('Register',related_name='name',on_delete=models.CASCADE,default=True)

    class Meta:
        ordering = ['-date_added']

    def __str__(self):
        return self.name
