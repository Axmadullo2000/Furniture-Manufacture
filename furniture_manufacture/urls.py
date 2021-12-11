from django.conf import settings
from django.conf.urls import url
from django.contrib import admin
from django.conf.urls.static import static
from django.urls import path, include
from django.views.static import serve

urlpatterns = [
                  path('admin/', admin.site.urls),
                  url(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
                  url(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT}),
                  path('', include('product.urls')),
                  path('', include('category.urls')),
                  path('', include('account.urls')),
              ]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
