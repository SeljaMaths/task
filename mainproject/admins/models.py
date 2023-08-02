from django.db import models

# Create your models here.


class employee(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=20,unique=True)
    password = models.CharField(max_length=20)
    task1 = models.CharField(max_length=100,null=True)
    task2 = models.CharField(max_length=100, null=True)
    task3 = models.CharField(max_length=100, null=True)


