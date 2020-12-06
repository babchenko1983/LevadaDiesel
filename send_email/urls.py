from django.urls import path
from . import views

urlpatterns = [

    path('sent/', views.index2),
]
