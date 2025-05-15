# forms.py
from django import forms

from .models import CarReview



CAR_BODY_CHOICES = [
    ("sedan", "Седан"),
    ("hatchback", "Хэтчбек"),
    ("wagon", "Универсал"),
    ("suv", "Внедорожник (SUV)"),
    ("crossover", "Кроссовер"),
    ("minivan", "Минивэн"),
    ("coupe", "Купе"),
    ("pickup", "Пикап"),
    ("convertible", "Кабриолет"),
]




CAR_DRIVE_CHOICES = [
    ("front", "Передний"),
    ("rear", "Задний"),
    ("all", "Полный"),
]




CAR_BRANDS = [
    ("Toyota", "Toyota"),
    ("Honda", "Honda"),
    ("Ford", "Ford"),
    ("Chevrolet", "Chevrolet"),
    ("BMW", "BMW"),
    ("Mercedes-Benz", "Mercedes-Benz"),
    ("Audi", "Audi"),
    ("Nissan", "Nissan"),
    ("Hyundai", "Hyundai"),
    ("Kia", "Kia"),
    ("Volkswagen", "Volkswagen"),
    ("Tesla", "Tesla"),
    ("Mazda", "Mazda"),
    ("Subaru", "Subaru"),
    ("Lexus", "Lexus"),
    ("Jeep", "Jeep"),
    ("GMC", "GMC"),
    ("Dodge", "Dodge"),
    ("Ram", "Ram"),
    ("Porsche", "Porsche"),
    ("Land Rover", "Land Rover"),
    ("Volvo", "Volvo"),
    ("Acura", "Acura"),
    ("Infiniti", "Infiniti"),
    ("Cadillac", "Cadillac"),
    ("Lincoln", "Lincoln"),
    ("Buick", "Buick"),
    ("Chrysler", "Chrysler"),
    ("Mitsubishi", "Mitsubishi"),
    ("Jaguar", "Jaguar"),
    ("Alfa Romeo", "Alfa Romeo"),
    ("Fiat", "Fiat"),
    ("Mini", "Mini"),
    ("Smart", "Smart"),
    ("Suzuki", "Suzuki"),
    ("Isuzu", "Isuzu"),
    ("Saab", "Saab"),
    ("Peugeot", "Peugeot"),
    ("Renault", "Renault"),
    ("Citroen", "Citroen"),
    ("Skoda", "Skoda"),
    ("Seat", "Seat"),
    ("Opel", "Opel"),
    ("Dacia", "Dacia"),
    ("Holden", "Holden"),
    ("Daewoo", "Daewoo"),
    ("Rover", "Rover"),
    ("MG", "MG"),
    ("Lada", "Lada"),
    ("Moskvich", "Moskvich"),
    ("Aston Martin", "Aston Martin"),
    ("Bentley", "Bentley"),
    ("Bugatti", "Bugatti"),
    ("Ferrari", "Ferrari"),
    ("Lamborghini", "Lamborghini"),
    ("Maserati", "Maserati"),
    ("Rolls-Royce", "Rolls-Royce"),
    ("McLaren", "McLaren"),
    ("Lotus", "Lotus"),
    ("Genesis", "Genesis"),
    ("Polestar", "Polestar"),
    ("Rivian", "Rivian"),
    ("Lucid", "Lucid"),
    ("BYD", "BYD"),
    ("Nio", "Nio"),
    ("XPeng", "XPeng"),
    ("Geely", "Geely"),
    ("Great Wall", "Great Wall"),
    ("Chery", "Chery"),
    ("Tata", "Tata"),
    ("Mahindra", "Mahindra"),
    ("Tata Motors", "Tata Motors"),
    ("Maruti Suzuki", "Maruti Suzuki"),
    ("Daihatsu", "Daihatsu"),
    ("Subaru", "Subaru"),
    ("SsangYong", "SsangYong"),
    ("Proton", "Proton"),
    ("Perodua", "Perodua"),
    ("Haval", "Haval"),
    ("Wuling", "Wuling"),
    ("Dongfeng", "Dongfeng"),
    ("FAW", "FAW"),
    ("BAIC", "BAIC"),
    ("GAC", "GAC"),
    ("SGMW", "SGMW"),
    ("Changan", "Changan"),
    ("JAC", "JAC"),
    ("Zotye", "Zotye"),
    ("Lifan", "Lifan"),
    ("Baojun", "Baojun"),
    ("Wey", "Wey"),
    ("Cupra", "Cupra"),
    ("DS Automobiles", "DS Automobiles"),
    ("Alpine", "Alpine"),
    ("Morgan", "Morgan"),
    ("TVR", "TVR"),
    ("Rimac", "Rimac"),
    ("Pagani", "Pagani"),
    ("Koenigsegg", "Koenigsegg"),
    ("Zenvo", "Zenvo"),
    ("Caterham", "Caterham"),
    ("Ariel", "Ariel"),
    ("BAC", "BAC"),
    ("Spyker", "Spyker"),
    ("Noble", "Noble"),
    ("Tesla", "Tesla"),
]






class SignUpForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)

class CarForm(forms.Form):
    car_brand = forms.ChoiceField(choices=CAR_BRANDS, label="Car Brand")  # Используем ChoiceField
    car_body = forms.ChoiceField(choices=CAR_BODY_CHOICES, label="Car Body")
    horse_power = forms.IntegerField(label="Horse Power", min_value=1)
    car_drive = forms.ChoiceField(choices=CAR_DRIVE_CHOICES, label="Car Drive")
    tax = forms.FloatField(label="Tax",  min_value=1)
    image_url = forms.URLField(label="Image URL", required=False)
    description = forms.CharField(max_length=255, required=False, label="Description", widget=forms.Textarea)

class CarImageForm(forms.Form):
    image = forms.ImageField(label="Car Image")


class ReviewForm(forms.Form):
    text = forms.CharField(widget=forms.Textarea, label="Your Review")
    likes = forms.IntegerField(label="Likes", initial=0)
    dislikes = forms.IntegerField(label="Dislikes", initial=0)


