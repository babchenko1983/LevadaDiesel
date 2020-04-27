from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('i18n/', include('django.conf.urls.i18n')),
    # path('', include('web.urls')),
    # path('cart/', include('carts.urls')),
    # path('checkout/', include('orders.urls')),
]

urlpatterns += i18n_patterns(
    path('admin/', admin.site.urls),
    path('cart/', include('carts.urls')),
    path('', include('web.urls')),
    path('checkout/', include('orders.urls')),
)


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += staticfiles_urlpatterns()
