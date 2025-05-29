from django.db import models


class Item(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.IntegerField(help_text="Price in cents")

    @property
    def display_price(self):
        return "{:.2f}".format(self.price / 100)

    def __str__(self):
        return self.name
