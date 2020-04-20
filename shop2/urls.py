from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


from carts import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('cart/', include('carts.urls')),
    path('', include('web.urls')),
    path('checkout/', include('orders.urls'))

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += staticfiles_urlpatterns()