# views.py
from django.shortcuts import render
from .models import Car

def car_list(request):
    cars = Car.objects.all()
    context = {'cars': cars}
    return render(request, 'car_list.html', context) # Make sure to pass ".html" to file name