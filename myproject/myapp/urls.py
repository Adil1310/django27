from django.urls import path
from . import views

urlpatterns = [
    path('', views.create_view, name='create'),
    path('success/', views.success_view, name='success'),
    path('icecream/add/', views.add_icecream, name='add-icecream'),
]