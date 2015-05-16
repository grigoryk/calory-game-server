from django.contrib import admin

from .models import Image, NutritionalData, Dish, Guess

admin.site.register(Image)
admin.site.register(NutritionalData)
admin.site.register(Dish)
admin.site.register(Guess)
