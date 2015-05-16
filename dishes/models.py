from django.db import models

from django.contrib.auth.models import User


class Image(models.Model):
    image = models.ImageField(upload_to="dish_images")

    created_at = models.DateTimeField(auto_now_add=True)


class NutritionalData(models.Model):
    calories = models.IntegerField(blank=True, null=True)
    fat = models.IntegerField(blank=True, null=True)
    carbohydrates = models.IntegerField(blank=True, null=True)
    protein = models.IntegerField(blank=True, null=True)

    last_modified = models.DateTimeField(auto_now=True)


class Dish(models.Model):
    author = models.ForeignKey(User)
    description = models.TextField()
    photos = models.ManyToManyField(Image)
    is_vegetarian = models.BooleanField()

    created_at = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

    nutritional_data = models.ForeignKey(
        NutritionalData, blank=True, null=True)

    class Meta:
        verbose_name_plural = "Dishes"


class Guess(models.Model):
    user = models.ForeignKey(User)
    dish = models.ForeignKey(Dish)
    created_at = models.DateTimeField(auto_now_add=True)

    nutritional_data = models.ForeignKey(NutritionalData)

    class Meta:
        verbose_name_plural = "Guesses"
