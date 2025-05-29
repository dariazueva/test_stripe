from django.contrib import admin

from . import models


@admin.register(models.Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "description",
        "price",
    )


@admin.register(models.Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ("created_at",)
    filter_horizontal = ("items",)
