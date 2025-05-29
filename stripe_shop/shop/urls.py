from django.urls import path

from . import views

urlpatterns = [
    path("item/<int:id>/", views.item_detail, name="item"),
    path("buy/<int:id>/", views.buy_item, name="buy_item"),
    path("success/", views.success_view, name="success"),
    path("cancel/", views.cancel_view, name="cancel"),
    path("order/<int:id>/", views.order_detail, name="order"),
    path("buy-order/<int:id>/", views.buy_order, name="buy_order"),
]
