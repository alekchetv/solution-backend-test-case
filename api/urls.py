from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import FoodViewSet


urlpatterns = [
   path("foods/", FoodViewSet.as_view(), name="food-list"),

]