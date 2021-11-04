from django.shortcuts import get_object_or_404, redirect, render
from . models import Item, Cart
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.
def items(request):
    fooditems = Item.objects.order_by('-last_modified')
    category_search = Item.objects.values_list('category', flat=True).distinct()
    context = {
        'fooditems' : fooditems,
        'category_search' : category_search,
    }
    return render(request, 'fooditems/items.html', context)



def single(request, item_id):
    item = get_object_or_404(Item, pk=item_id)
    context = {
        'item' : item,
    }
    return render(request, 'fooditems/single.html', context)



def search(request):
    items = Item.objects.order_by('-last_modified')
    category_search = Item.objects.values_list('category', flat=True).distinct()
    if 'keyword' in request.GET:
        data = request.GET['keyword']
        if data:
            items = items.filter(description__icontains=data) | items.filter(name__icontains=data)

    if 'category' in request.GET:
        data = request.GET['category']
        if data:
            items = items.filter(category__iexact=data)

    if 'diet' in request.GET:
        data = request.GET['diet']
        if data:
            if data == 'veg':
                items = items.filter(is_veg=True)
            else:
                items = items.filter(is_veg=False)

    context = {
        'items' : items,
        'category_search' : category_search,
    }
    return render(request, 'fooditems/search.html', context)


@login_required(login_url='login')
def cart(request):
    cart_items = Cart.objects.filter(user=request.user)
    total = 0

    for item in cart_items:
        total += item.food.price * item.quantity

    context = {
        'cart_items' : cart_items,
        'total' : total,
    }
    return render(request, 'fooditems/cart.html', context)


@login_required(login_url='login')
def add_to_cart(request, item_id):
    item = get_object_or_404(Item, pk=item_id)
    obj = Cart(user=request.user, food=item)
    obj.save()
    messages.success(request, 'Added to cart successfullly')
    return redirect('items')


@login_required(login_url='login')
def remove_from_cart(request, id):
    obj = get_object_or_404(Cart, pk=id)
    obj.delete()
    messages.success(request, "Removed from cart successfully")
    return redirect('cart')

def update_cart(request, id):
    obj = get_object_or_404(Cart, pk=id)
    if request.method == 'POST':
        quantity = request.POST['quantity']

        obj.quantity = quantity
        obj.save()
        return redirect('cart')

    return render(request, 'fooditems/cart.html')