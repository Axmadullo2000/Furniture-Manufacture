from django.urls import path

from product.views import home, Store, product_detail, search

urlpatterns = [
    path('', home, name='home'),
    path('category/<slug:category_slug>/', Store, name='products_by_category'),
    path('category/<slug:category_slug>/<slug:product_slug>/', product_detail, name='product_info'),
    path('search/', search, name='search')
]
