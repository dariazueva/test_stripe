from django.urls import path

from . import views

urlpatterns = [
    path("item/<int:id>/", views.item_detail, name="item"),
    path("buy/<int:id>/", views.buy_item, name="buy_item"),
    path("success/", views.success_view, name="success"),
    path("cancel/", views.cancel_view, name="cancel"),
]
