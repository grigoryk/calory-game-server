from rest_framework import viewsets
from .serializers import DishSerializer
from ..models import Dish


class DishViewSet(viewsets.ModelViewSet):
    queryset = Dish.objects.all()
    serializer_class = DishSerializer
