from django import forms


class TestForm(forms.Form):
    text_field = forms.CharField(
        label="Тестовое поле ввода",
        max_length=63,
        min_length=3,
        required=True
    )

    age_field = forms.IntegerField(
        label="Возраст",
        min_value=14,
        max_value=90,
        required=True
    )

    password_field = forms.CharField(
        label="Пароль",
        widget=forms.PasswordInput,
        max_length=32,
        min_length=8,
        required=True
    )

    email_field = forms.EmailField(
        label="Email",
        max_length=128,
        required=True
    )

    choice_field = forms.ChoiceField(
        label="Выберите нужный вариант:",
        choices=[
            ('option1', 'Вариант 1'),
            ('option2', 'Вариант 2'),
            ('option3', 'Вариант 3'),
        ],
        required=True
    )



    date_field = forms.DateField(
        label="Date",
        widget=forms.DateInput(attrs={'type': 'date'}),  # Use HTML5 date picker
        required=False
    )