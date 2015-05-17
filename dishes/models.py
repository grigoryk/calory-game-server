from django.db import models

from django.contrib.auth.models import User


class Image(models.Model):
    image = models.ImageField(upload_to="dish_images")

    created_at = models.DateTimeField(auto_now_add=True)


class Dish(models.Model):
    author = models.ForeignKey(User)
    description = models.TextField()
    images = models.ManyToManyField(Image)
    is_vegetarian = models.BooleanField()

    created_at = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "Dishes"


class Guess(models.Model):
    user = models.ForeignKey(User)
    dish = models.ForeignKey(Dish)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Guesses"


class NutritionalData(models.Model):
    calories = models.IntegerField(blank=True, null=True)
    fat = models.IntegerField(blank=True, null=True)
    carbohydrates = models.IntegerField(blank=True, null=True)
    protein = models.IntegerField(blank=True, null=True)

    last_modified = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class NutritionalDataDish(NutritionalData):
    dish = models.OneToOneField(Dish, related_name="nutritional_data")


class NutritionalDataGuess(NutritionalData):
    guess = models.OneToOneField(Guess, related_name="nutritional_data")
