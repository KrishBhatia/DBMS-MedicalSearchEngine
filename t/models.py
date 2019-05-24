from django.db import models
from django.core.validators import MaxLengthValidator, MinLengthValidator

class Symptom(models.Model):
    name = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.name


class Store(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.BigIntegerField()
    city = models.CharField(max_length=30)
    location = models.CharField(max_length=200)
    pincode = models.PositiveIntegerField()

    def __str__(self):
        return self.name


class Medicine(models.Model):
    name = models.CharField(max_length=100, primary_key=True)
    drug = models.CharField(max_length=200)
    type = models.CharField(max_length=30)
    # description = models.TextField()
    stores = models.ManyToManyField(Store)

    def __str__(self):
        return self.name


class Disease(models.Model):
    name = models.CharField(max_length=50, primary_key=True)
    description = models.TextField()
    symptoms = models.ManyToManyField(Symptom)
    medicines = models.ManyToManyField(Medicine)

    def __str__(self):
        return self.name
