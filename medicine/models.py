from django.db import models
from accounts.models import Peracik
# Create your models here.

class Medicine(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='medicine')
    description = models.TextField()
    ingredients = models.ManyToManyField('ingredient.Ingredient')
    peracik = models.ForeignKey(Peracik, on_delete=models.CASCADE)
    message_status = models.CharField(max_length=255, blank=True, null=True)
    usage_rules = models.TextField()
    ways_to_use = models.TextField()
    class Status(models.TextChoices):
        CANCELED = 'CANCELED'
        WAITING = 'WAITING'
        ACCEPTED = 'ACCEPTED'
    status = models.CharField(max_length=10, choices=Status.choices, default=Status.WAITING)
    def __str__(self):
        return self.name