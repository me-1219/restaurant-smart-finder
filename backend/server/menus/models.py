from django.db import models
from restaurants.models import Restaurant


class Menu(models.Model):

    restaurant = models.ForeignKey(
        Restaurant,
        on_delete=models.CASCADE,
        related_name="menus"
    )

    food_name = models.CharField(max_length=200)

    category = models.CharField(max_length=100)

    price = models.DecimalField(max_digits=6, decimal_places=2)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.food_name
