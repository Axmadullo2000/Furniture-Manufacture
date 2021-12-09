from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth import logout, login
from account.models import Cart, CartItem
from category.models import Category
from product.models import Product
from specifications.models import Specification


class RegisterUser(CreateView):
    form_class = UserCreationForm
    template_name = 'account/register.html'
    success_url = reverse_lazy('login')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        return dict(list(context.items()))

    def get_success_url(self):
        return reverse_lazy('home')

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('home')


class LoginUser(LoginView):
    form_class = AuthenticationForm
    template_name = 'account/login.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        return dict(list(context.items()))


def logout_user(request):
    logout(request)
    return redirect('login')


def _cart_id(request):
    card = request.session.session_key
    if not card:
        card = request.session.create()
    return card

#telegram bot
# def place_order(request):
#     bot = telebot.TeleBot('AAH3mBSy83YZGLyXjSXCZ2gJVGDzZb6GKYc')
#     card = Cart.objects.get(cart_id=_cart_id(request))
#     card_items = CartItem.objects.filter(cart=card, is_active=True)
#     product_name = card_items.product.product_name
#     print(product_name)
#     text = f'{request.user} {card_items.product.product_name}'
#     # O`zingizni telegram idngiz
#     bot.send_message(5087867519, text=text)
#     card_items.delete()
#     return redirect('home')


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


def logout_request(request):
    logout(request)
    messages.info(request, "You have successfully logged out.")
    return redirect("home")


def about_us(request):
    return render(request, 'main_pages/about_us.html')


def how_it_works(request):
    return render(request, 'main_pages/howitworks.html')
