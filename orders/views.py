from django.shortcuts import render, redirect, get_object_or_404
from .models import MenuItem, Order, OrderItem

def order_view(request):
    menu = MenuItem.objects.all()
    if request.method == 'POST':
        order = Order.objects.create()
        for item in menu:
            qty = int(request.POST.get(str(item.id), 0))
            if qty > 0:
                OrderItem.objects.create(order=order, menu_item=item, quantity=qty)
        order.status = 'preparing'
        order.save()
        return redirect('order_status_list') 
    return render(request, 'orders/order_form.html', {'menu': menu})


def order_status_list_view(request):
    recent_orders = Order.objects.order_by('-created_at')[:10]
    return render(request, 'orders/status_list.html', {'orders': recent_orders})


def kitchen_view(request):
    orders = Order.objects.filter(status__in=['preparing', 'pending'])
    if request.method == 'POST':
        order_id = request.POST.get('order_id')
        order = Order.objects.get(id=order_id)
        order.status = 'ready'
        order.save()
        return redirect('kitchen')
    return render(request, 'orders/kitchen.html', {'orders': orders})


def billing_view(request):
    ready_orders = Order.objects.filter(status='ready')
    if request.method == 'POST':
        order_id = request.POST.get('order_id')
        order = Order.objects.get(id=order_id)
        total = order.total_amount()
        
        if order.status != 'completed':
            order.status = 'completed'
            order.save()

        
        if request.GET.get("print") == "true":
            return render(request, 'orders/billing.html', {
                'orders': ready_orders,
                'bill': total,
                'billed_order': order,
            })

        return redirect('order_status_list')

    return render(request, 'orders/billing.html', {'orders': ready_orders})

