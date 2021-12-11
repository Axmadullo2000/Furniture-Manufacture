from django.contrib import messages
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import logout, login, authenticate

from account.forms import UserRegisterForm
from account.models import Cart, CartItem
from category.models import Category
from product.models import Product
from specifications.models import Specification
import requests


def _cart_id(request):
    card = request.session.session_key
    if not card:
        card = request.session.create()
    return card


def place_order(request):
    card = Cart.objects.get(cart_id=_cart_id(request))
    card_items = CartItem.objects.filter(cart=card, is_active=True)
    user = User.objects.get(username=request.user)
    text = f'\t\t\tКлиент -> {request.user} \n \t\t\tпочтовый адрес -> {user.email}'
    for i in card_items:
        text += f"\n\n\t\t\t\t\t\t\tКупленные мебели: \n\nНазвание -> {i.product.product_name} \n\nКоличество -> {i.quantity} " \
                f"\n\nЦена Мебели -> {i.product.price} $ \n\nТакси -> {i.percent()} \n\nОбщая сумма -> {i.over_all()} $"
    requests.get(url=f'https://api.telegram.org/bot5098300808:AAGlUoW8u_D7y8hpOPkrTmhfUMlMkC8Qgig/sendMessage?chat_id'
                     f'=849928658&text={text}')
    card_items.delete()
    return redirect('condition_order')


def condition_order(request):
    return render(request, 'place_order.html')


def cart(request, total=0, quantity=0, card_items=None):
    category = Category.objects.all()
    specification = Specification.objects.all()
    try:
        card = Cart.objects.get(cart_id=_cart_id(request))
        card_items = CartItem.objects.filter(cart=card, is_active=True)
        cart_count = card_items.count()
        for cart_item in card_items:
            total += (cart_item.product.price * cart_item.quantity)
            quantity += cart_item.quantity
        taxi = (2 * total) / 100
        grand_total = taxi + total
    except Exception as e:
        raise e

    context = {
        'total': total,
        'cart_count': cart_count,
        'quantity': quantity,
        'cart_items': card_items,
        'taxi': taxi,
        'grand_total': grand_total,
        'categories': category,
        'specifications': specification,
    }
    return render(request, 'cart.html', context)


def add_cart(request, product_id):
    product = Product.objects.get(id=product_id)
    try:
        card = Cart.objects.get(cart_id=_cart_id(request))
    except Cart.DoesNotExist:
        card = Cart.objects.create(
            cart_id=_cart_id(request)
        )
    card.save()
    try:
        card_item = CartItem.objects.get(product=product, cart=card)
        card_item.quantity += 1
        card_item.save()
    except CartItem.DoesNotExist:
        card_item = CartItem.objects.create(
            product=product,
            quantity=1,
            cart=card,
        )
        card_item.save()
    return redirect('cart')


def product_detail(request):
    category = Category.objects.all()
    products = Product.objects.all()
    context = {
        'categories': category,
        'products': products
    }
    return render(request, 'index.html', context)


def remove_cart(request, product_id):
    card = Cart.objects.get(cart_id=_cart_id(request))
    product = get_object_or_404(Product, id=product_id)
    card_item = CartItem.objects.get(product=product, cart=card)
    if card_item.quantity > 1:
        card_item.quantity -= 1
        card_item.save()
    else:
        card_item.delete()
    return redirect('cart')


def remove_cart_item(request, product_id):
    card = Cart.objects.get(cart_id=_cart_id(request))
    product = get_object_or_404(Product, id=product_id)
    card_item = CartItem.objects.get(product=product, cart=card)
    card_item.delete()
    return redirect('cart')


def register(request):
    template_name = 'account/register.html'
    form = UserRegisterForm()
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():  # addded profile form
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, f'Account created for user {user}!')
            return redirect('login')
    context = {
        'form': form
    }
    return render(request, template_name, context)


def log_in(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Username OR password is incorrect')

    return render(request, 'account/login.html')


def log_out(request):
    logout(request)
    return redirect('login')


def about_us(request):
    return render(request, 'main_pages/about_us.html')


def how_it_works(request):
    return render(request, 'main_pages/howitworks.html')
