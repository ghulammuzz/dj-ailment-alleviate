from django.db import models

# Create your models here.

class Ingredient(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='ingredient', blank=True, null=True)
    description = models.TextField()
    class Status(models.TextChoices):
        CANCELED = 'CANCELED'
        WAITING = 'WAITING'
        ACCEPTED = 'ACCEPTED'
    status = models.CharField(max_length=10, choices=Status.choices, default=Status.WAITING)
    medicine_many = models.ManyToManyField('medicine.Medicine', blank=True)
    category = models.ForeignKey('category.Category', on_delete=models.SET_NULL, null=True, blank=True)
    
    def __str__(self):
        return self.name
    