from django.urls import path
from account.views import add_cart, cart, remove_cart_item, remove_cart, product_detail, RegisterUser, LoginUser, \
    logout_user, about_us, how_it_works

urlpatterns = [
    path('card/', cart, name='cart'),
    path('add-cart/<int:product_id>/', add_cart, name='add_cart'),
    path('category/<slug:category_slug>/', product_detail, name='product_detail'),
    path('remove_cart/<int:product_id>/', remove_cart, name='remove_cart'),
    path('remove_cart_item/<int:product_id>/', remove_cart_item, name='remove_cart_item'),
    path('register/', RegisterUser.as_view(), name='register'),
    path('login/', LoginUser.as_view(), name='login'),
    # path('place_order/', place_order, name='place_order'),
    path('logout/', logout_user, name='logout'),
    path('about_us/', about_us, name='about_us'),
    path('how_it_works/', how_it_works, name='how_it_works')
]
