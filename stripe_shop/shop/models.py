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


class Order(models.Model):
    items = models.ManyToManyField(Item, verbose_name="Items")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order #{self.pk}"

    def total_amount(self):
        return sum(item.price for item in self.items.all()) / 100
