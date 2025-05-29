import stripe
from django.conf import settings
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render

from .models import Item, Order

stripe.api_key = settings.STRIPE_SECRET_KEY


def item_detail(request, id):
    item = get_object_or_404(Item, id=id)
    return render(
        request,
        "item.html",
        {"item": item, "stripe_public_key": settings.STRIPE_PUBLISHABLE_KEY},
    )


def buy_item(request, id):
    item = get_object_or_404(Item, id=id)
    session = stripe.checkout.Session.create(
        payment_method_types=["card"],
        line_items=[
            {
                "price_data": {
                    "currency": "usd",
                    "product_data": {"name": item.name},
                    "unit_amount": item.price,
                },
                "quantity": 1,
            }
        ],
        mode="payment",
        success_url="http://localhost:8000/success",
        cancel_url="http://localhost:8000/cancel",
    )
    return JsonResponse({"id": session.id})


def success_view(request):
    return render(request, "success.html")


def cancel_view(request):
    return render(request, "cancel.html")


def order_detail(request, id):
    order = get_object_or_404(Order, id=id)
    return render(
        request,
        "order.html",
        {"order": order, "stripe_public_key": settings.STRIPE_PUBLISHABLE_KEY},
    )


def buy_order(request, id):
    order = get_object_or_404(Order, id=id)
    line_items = []
    for item in order.items.all():
        line_items.append(
            {
                "price_data": {
                    "currency": "usd",
                    "product_data": {"name": item.name},
                    "unit_amount": item.price,
                },
                "quantity": 1,
            }
        )
    session = stripe.checkout.Session.create(
        payment_method_types=["card"],
        line_items=line_items,
        mode="payment",
        success_url="http://localhost:8000/success",
        cancel_url="http://localhost:8000/cancel",
    )
    return JsonResponse({"id": session.id})
