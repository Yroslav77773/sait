# views.py
from django.shortcuts import render
from .models import Car

def car_list(request):
    cars = Car.objects.all()
    context = {'cars': cars}
    return render(request, 'car_list.html', context)


# views.py
from django.shortcuts import render
from .models import CarReview

def car_review_list(request):
    """
    Получает список ВСЕХ обзоров.  УПРОЩЕННЫЙ ВАРИАНТ.
    """
    reviews = CarReview.objects.all() # Получаем все обзоры из базы данных
    context = {'reviews': reviews}  # Передаём обзоры в шаблон
    return render(request, 'car_review_list.html', context)