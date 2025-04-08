# views.py
from django.shortcuts import render
from .models import Car
from .models import CarReview

def car_list(request):
    cars = Car.objects.all()
    context = {'cars': cars}
    return render(request, 'car_list.html', context)



def car_review_list(request):
    reviews = CarReview.objects.all()
    context = {'reviews': reviews}
    return render(request, 'car_review_list.html', context)