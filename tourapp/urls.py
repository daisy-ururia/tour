from django.contrib import admin
from django.urls import path
from tourapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', views.index, name='index'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
    path('elements', views.elements, name='elements'),
    path('services', views.services, name='services'),
    path('success', views.success, name='success'),
    path('', views.signup, name='signup'),
    path('login', views.login_view, name='login'),
]
