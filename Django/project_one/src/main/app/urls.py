from django.urls import path, include
from rest_framework import routers
from .views import BookViewSet, TableViewSet

router = routers.DefaultRouter()
router.register('books',BookViewSet)
router.register('tables',TableViewSet)
# from .views import Another,Tables
urlpatterns = [
    path('',include(router.urls)),
    # path('another/', Another.as_view()),
    # path('tables/', Tables.as_view()),
]