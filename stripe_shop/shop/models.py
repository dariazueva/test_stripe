from django.db import models


class Item(models.Model):
    name = models.CharField("Наименование", max_length=255)
    description = models.TextField("Описание")
    price = models.IntegerField("Цена", help_text="в центах")

    @property
    def display_price(self):
        return "{:.2f}".format(self.price / 100)

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"

    def __str__(self):
        return self.name
