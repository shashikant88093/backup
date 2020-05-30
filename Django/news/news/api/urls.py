from django.urls import path,include
from rest_framework import routers
from .views import TableList,ReadFile
router = routers.DefaultRouter()
router.register('table',TableList)
router.register('readfile',ReadFile)
urlpatterns = [
    path('',include(router.urls)),
]