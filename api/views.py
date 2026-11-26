from django.shortcuts import render
from .models import Food, FoodCategory, FoodListSerializer
from rest_framework import generics
from django.db.models import Prefetch


class FoodViewSet(generics.ListAPIView):
    queryset = (
        FoodCategory.objects
        .filter(food__is_publish=True)
        .prefetch_related(
            Prefetch("food", queryset=Food.objects.filter(is_publish=True))
        )
        .distinct()
        .order_by("order_id")
    )
    serializer_class = FoodListSerializer
    pagination_class = None   