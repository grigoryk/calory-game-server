from rest_framework import serializers
from ..models import (
    Dish, Guess, Image, NutritionalDataDish, NutritionalDataGuess)


class NutritionalDataDishSerializer(serializers.ModelSerializer):
    class Meta:
        model = NutritionalDataDish
        fields = (
            'calories', 'fat', 'carbohydrates', 'protein', 'last_modified')


class NutritionalDataGuessSerializer(NutritionalDataDishSerializer):
    class Meta:
        model = NutritionalDataGuess


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ('image', 'created_at')


class DishSerializer(serializers.HyperlinkedModelSerializer):
    images = ImageSerializer(many=True, read_only=True)
    nutritional_data = NutritionalDataDishSerializer(
        many=False, read_only=True)

    class Meta:
        model = Dish
        fields = (
            'description', 'images', 'is_vegetarian', 'created_at',
            'last_modified', 'nutritional_data'
        )


class GuessSerializer(serializers.HyperlinkedIdentityField):
    nutritional_data = NutritionalDataGuessSerializer(
        many=False, read_only=True)

    class Meta:
        model = Guess
        fields = ('user', 'dish', 'created_at', 'nutritional_data')
