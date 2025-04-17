"""
URL configuration for libaries project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from accounts import views as account_views
from books import views as book_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('signup/', account_views.admin_signup, name='admin_signup'),
    path('login/', account_views.admin_login, name='admin_login'),
    path('logout/', account_views.admin_logout, name='admin_logout'),
    path('', book_views.book_list, name='book_list'),
    path('books/add/', book_views.book_create, name='book_create'),
    path('books/<int:pk>/edit/', book_views.book_update, name='book_update'),
    path('books/<int:pk>/delete/', book_views.book_delete, name='book_delete'),
]