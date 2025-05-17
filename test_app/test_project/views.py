from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login as auth_login, logout as auth_logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.http import HttpResponse
from django.contrib import messages
from .models import Car, CarReview
from .forms import CarForm, CarImageForm, ReviewForm
from django.contrib import messages

# Функция для отображения списка автомобилей с возможностью поиска
def car_list(request):
    # Получаем поисковый запрос из параметров GET (если есть)
    search_query = request.GET.get('search_query', '')
    # Получаем все автомобили из базы данных
    cars = Car.objects.all()

    # Если есть поисковый запрос, фильтруем автомобили по марке (без учета регистра)
    if search_query:
        cars = cars.filter(car_brand__icontains=search_query)

    # Создаем контекст для передачи в шаблон
    context = {'cars': cars, 'search_query': search_query}
    # Отображаем шаблон car_list.html с переданными данными
    return render(request, 'car_list.html', context)

# Функция для отображения страницы выбора способа входа
def login_choice(request):
    # Просто отображаем шаблон login_choice.html
    return render(request, 'login_choice.html')

# Функция для обработки входа пользователя
def login_view(request):
    if request.method == 'POST':  # Если запрос POST (отправка формы)
        # Создаем форму аутентификации с данными из запроса
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():  # Если данные формы валидны
            user = form.get_user()  # Получаем пользователя из формы
            auth_login(request, user)  # Выполняем вход пользователя
            return redirect('car_list')  # Перенаправляем на список автомобилей
        else:
            # Если форма невалидна, показываем ее с ошибками
            return render(request, 'login.html', {'form': form})
    else:  # Если запрос GET (просто открытие страницы)
        # Создаем пустую форму аутентификации
        form = AuthenticationForm()
        return render(request, 'login.html', {'form': form})

# Функция для обработки регистрации пользователя
def signup(request):
    if request.method == 'POST':  # Если запрос POST (отправка формы)
        # Создаем форму регистрации с данными из запроса
        form = UserCreationForm(request.POST)
        if form.is_valid():  # Если данные формы валидны
            user = form.save()  # Сохраняем нового пользователя
            auth_login(request, user)  # Выполняем вход нового пользователя
            return redirect('car_list')  # Перенаправляем на список автомобилей
        else:
            # Если форма невалидна, показываем ее с ошибками
            return render(request, "signup.html", {
                "form": form,
                "title": "Sign Up",
                "errors": form.errors,
            })
    else:  # Если запрос GET (просто открытие страницы)
        # Показываем пустую форму регистрации
        return render(request, "signup.html", {
            "form": UserCreationForm(),
            "title": "Sign Up",
        })

# Функция для выхода пользователя
def logout_view(request):
    auth_logout(request)  # Выполняем выход пользователя
    return redirect('car_list')  # Перенаправляем на список автомобилей

# Функция для отображения профиля пользователя
def profile(request):
    # Просто отображаем шаблон profile.html
    return render(request, 'profile.html')

# Функция для добавления автомобиля (только для авторизованных пользователей)
@login_required
def add_car(request):
    if request.method == 'POST':  # Если запрос POST (отправка формы)
        car_form = CarForm(request.POST)  # Создаем форму с данными
        if car_form.is_valid():  # Если данные формы валидны
            # Получаем очищенные данные из формы
            description = car_form.cleaned_data['description']
            car_brand = car_form.cleaned_data['car_brand']
            car_model = car_form.cleaned_data['car_model']
            car_body = car_form.cleaned_data['car_body']
            horse_power = car_form.cleaned_data['horse_power']
            car_drive = car_form.cleaned_data['car_drive']
            tax = car_form.cleaned_data['tax']

            # Создаем и сохраняем новый автомобиль
            car = Car(
                description=description,
                car_brand=car_brand,
                car_model=car_model,
                car_body=car_body,
                horse_power=horse_power,
                car_drive=car_drive,
                tax=tax,
                user=request.user.username,  # Сохраняем имя текущего пользователя
            )
            car.save()

            return redirect('car_list')  # Перенаправляем на список автомобилей
    else:  # Если запрос GET (просто открытие страницы)
        car_form = CarForm()  # Создаем пустую форму

    return render(request, 'add_car.html', {'car_form': car_form})

# Функция для удаления автомобиля (только для авторизованных пользователей)
@login_required
def delete_car(request, car_id):
    # Получаем автомобиль по ID или возвращаем 404 если не найден
    car = get_object_or_404(Car, pk=car_id)
    car.delete()  # Удаляем автомобиль
    return redirect('car_list')  # Перенаправляем на список автомобилей

# Функция для добавления отзыва (только для авторизованных пользователей)
@login_required
def add_reviews(request, car_id):
    # Получаем автомобиль по ID или возвращаем 404 если не найден
    car = get_object_or_404(Car, pk=car_id)
    if request.method == 'POST':  # Если запрос POST (отправка формы)
        form = ReviewForm(request.POST)  # Создаем форму с данными
        if form.is_valid():  # Если данные формы валидны
            # Получаем очищенные данные из формы
            text = form.cleaned_data['text']
            likes = form.cleaned_data['likes']
            dislikes = form.cleaned_data['dislikes']

            # Создаем и сохраняем новый отзыв
            carreview = CarReview(
                car=car,
                contents=text,
                likes=likes,
                dislikes=dislikes
            )
            carreview.save()
            # Перенаправляем на список отзывов для этого автомобиля
            return redirect('car_review_list', car_id=car.id)
        else:
            # Если форма невалидна, показываем ее с ошибками
            return render(request, 'add_review.html', {'form': form, 'car': car})
    else:  # Если запрос GET (просто открытие страницы)
        form = ReviewForm()  # Создаем пустую форму
        return render(request, 'add_review.html', {'form': form, 'car': car})

# Функция для просмотра списка отзывов для конкретного автомобиля
def car_review_list(request, car_id):
    # Получаем автомобиль по ID или возвращаем 404 если не найден
    car = get_object_or_404(Car, pk=car_id)
    # Получаем все отзывы для этого автомобиля
    reviews = CarReview.objects.filter(car=car)
    # Отображаем шаблон с автомобилем и его отзывами
    return render(request, 'car_review_list.html', {'car': car, 'reviews': reviews})