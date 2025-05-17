"""
URL configuration for test_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from . import views

urlpatterns = [
    # Основные маршруты для автомобилей
    path('', views.car_list, name='car_list'),  # Главная страница (список автомобилей)
    path('cars/', views.car_list, name='car_list_alt'),  # Альтернативный URL для списка автомобилей
    path('add/', views.add_car, name='add_car'),  # Добавление автомобиля
    path('delete/<int:car_id>/', views.delete_car, name='delete_car'),  # Удаление автомобиля

    # Маршруты для отзывов
    path('car/<int:car_id>/reviews/', views.car_review_list, name='car_review_list'),  # Список отзывов
    path('car/<int:car_id>/add_review/', views.add_reviews, name='add_reviews'),  # Добавление отзыва

    # Аутентификация и профиль
    path('login_choice/', views.login_choice, name='login_choice'),  # Выбор способа входа
    path('login/', views.login_view, name='login'),  # Вход
    path('signup/', views.signup, name='signup'),  # Регистрация
    path('logout/', views.logout_view, name='logout'),  # Выход
    path('profile/', views.profile, name='profile'),  # Профиль

    # Админка
    path('admin/', admin.site.urls),
]