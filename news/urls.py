from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('article/<int:pk>/', views.article_detail, name='article_detail'),
    path('contact/', views.contact, name='contact'),
    path('support/', views.support, name='support'),
]
