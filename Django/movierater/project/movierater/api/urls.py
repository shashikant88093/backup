from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from rest_framework import routers
from .views import MovieViewSet, RatingViewSet, UserViewSet
router = routers.DefaultRouter()
router.register('user',UserViewSet)
router.register('movie',MovieViewSet)
router.register('rating',RatingViewSet)

urlpatterns = [
    path('', include(router.urls)),
]