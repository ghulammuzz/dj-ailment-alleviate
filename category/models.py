from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    # ingredients_many = models.ManyToManyField('ingredient.Ingredient', related_name='ingredients_many')

    def __str__(self):
        return self.name