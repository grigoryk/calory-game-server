from rest_framework import serializers
from ..models import Dish, Guess, Image, NutritionalData


class NutritionalData(serializers.ModelSerializer):
    class Meta:
        model = NutritionalData
        fields = (
            'calories', 'fat', 'carbohydrates', 'protein', 'last_modified')


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ('image', 'created_at')


class DishSerializer(serializers.HyperlinkedModelSerializer):
    images = ImageSerializer(many=True, read_only=True)
    nutritional_data = NutritionalData(many=False, read_only=True)

    class Meta:
        model = Dish
        fields = (
            'description', 'images', 'is_vegetarian', 'created_at',
            'last_modified', 'nutritional_data'
        )


class GuessSerializer(serializers.HyperlinkedIdentityField):
    nutritional_data = NutritionalData(many=False, read_only=True)

    class Meta:
        model = Guess
        fields = ('user', 'dish', 'created_at', 'nutritional_data')
