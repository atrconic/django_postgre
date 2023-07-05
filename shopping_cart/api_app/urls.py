from django.urls import path
from .views import CartItemViews, CartItemsViews

urlpatterns = [
    path('cart-items/', CartItemsViews.as_view()),
    path('cart-items/<int:id>', CartItemViews.as_view()),
]
