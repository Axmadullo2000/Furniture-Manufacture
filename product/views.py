from django.contrib.postgres.search import TrigramSimilarity
from django.shortcuts import render, get_object_or_404

from account.models import CartItem
from account.views import _cart_id
from category.models import Category
from product.models import Product


def home(request):
    category = Category.objects.all()
    products = Product.objects.all()
    context = {
        'categories': category,
        'products': products
    }
    return render(request, 'index.html', context)


def Store(request, category_slug=None):
    categories = None
    products = None
    if category_slug is not None:
        categories = get_object_or_404(Category, slug=category_slug)
        products = Product.objects.filter(category=categories, is_available=True).order_by('id')
        products_count = products.count()
    else:
        products = Product.objects.all().filter(is_available=True)
        products_count = products.count()
    category = Category.objects.all()
    context = {
        'products': products,
        'products_count': products_count,
        'categories': category
    }
    return render(request, 'index.html', context)


def product_detail(request, category_slug, product_slug):
    try:
        single_product = Product.objects.get(category__slug=category_slug, slug=product_slug)
        products = Product.objects.exclude(slug=product_slug). \
            annotate(similarity=TrigramSimilarity('product_name',
                                                  single_product.product_name)).filter(similarity__gt=0.3)
    except Exception as e:
        raise e
    try:
        single = Product.objects.get(category__slug=category_slug, slug=product_slug)
        in_cart = CartItem.objects.filter(cart__cart_id=_cart_id(request), product=single_product).exists()
    except Exception as e:
        raise e
    context = {
        'single_product': single,
        'products': products,
        'in_cart': in_cart,
    }
    return render(request, 'details/product_detail.html', context)


def search(request):
    products = None
    categories = Category.objects.all()
    if 'keyword' in request.GET:
        keyword = request.GET['keyword']
        if keyword:
            products = Product.objects.filter(
                product_name__contains=keyword
            )
        else:
            products = Product.objects.all()
        products_count = products.count()
    context = {
        'keyword': keyword,
        'products': products,
        'products_count': products_count,
        'categories': categories,
    }
    return render(request, 'index.html', context)
