from django.conf import settings
from django.contrib import admin
from django.conf.urls.static import static
from django.urls import path, include
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('product.urls')),
    path('', include('category.urls')),
    path('', include('account.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
