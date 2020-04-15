from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from .views import Search, ItemDetailView



urlpatterns = [

    path('', views.index, name='home'),
    path('shop/', views.shop, name='shop'),
    # path('/team/', views.team, name='team'),
    path('contact/', views.contact, name='contact'),
    path('search/', Search.as_view(), name='search'),
    path("<slug:slug>/", ItemDetailView.as_view(), name='single'),




]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)