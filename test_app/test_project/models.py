from django.db import models

class Car(models.Model):
    description = models.CharField(max_length=255, blank=True, null=True)
    car_brand = models.CharField(max_length=255)
    car_body = models.CharField(max_length=255)
    horse_power = models.IntegerField()
    car_drive = models.CharField(max_length=255)
    tax = models.FloatField(default=0)
    user = models.CharField(max_length=255)


    def __str__(self):
        return f"{self.car_brand} {self.car_body}"

class CarImage(models.Model):
    car = models.ForeignKey(Car, on_delete=models.DO_NOTHING, null=True)  # ID авто к которому относится изображение
    image_path = models.CharField(max_length=255)  # Путь к изображению

    def __str__(self):
        return self.image_path

class CarReview(models.Model):
    contents = models.TextField(default=0)  # Текст обзора
    likes = models.IntegerField(default=0)
    dislikes = models.IntegerField(default=0)
    author_id = models.IntegerField(default=0)  # ID пользователя, который написал обзор
    car = models.ForeignKey(Car, on_delete=models.DO_NOTHING, null=True)  # ID авто, к которому относится обзор

    def __str__(self):
        return self.contents