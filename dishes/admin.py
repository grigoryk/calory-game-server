from django.contrib import admin

from .models import (
    Image, NutritionalDataDish, NutritionalDataGuess, Dish, Guess)


class NutritionalDataDishInline(admin.StackedInline):
    model = NutritionalDataDish


class DishAdmin(admin.ModelAdmin):
    list_display = ('description', 'is_vegetarian', 'created_at')
    inlines = [NutritionalDataDishInline]


class NutritionalDataGuessInline(admin.StackedInline):
    model = NutritionalDataGuess


class GuessAdmin(admin.ModelAdmin):
    inlines = [NutritionalDataGuessInline]


admin.site.register(Image)
admin.site.register(Dish, DishAdmin)
admin.site.register(Guess, GuessAdmin)
