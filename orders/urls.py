from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("checkout/", views.order_create, name='checkout'),
    path("back/", views.back, name='back'),
    path("policy/", views.privacy_policy, name='policy'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

    urlpatterns += staticfiles_urlpatterns()
