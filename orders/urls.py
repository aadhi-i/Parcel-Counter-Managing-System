from django.urls import path
from . import views

urlpatterns = [
    path('order/', views.order_view, name='order'),
    path('status/', views.order_status_list_view, name='order_status_list'),
    path('kitchen/', views.kitchen_view, name='kitchen'),
    path('billing/', views.billing_view, name='billing'),
]
