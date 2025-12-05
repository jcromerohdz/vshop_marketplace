from django.contrib.auth import views as auth_views
from django.urls import path
from .views import contact, detail

urlpatterns = [
    path('contact/', contact, name='contact'),
    path('detail/<int:pk>/', detail, name='detail'),
]