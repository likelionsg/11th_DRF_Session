from django.urls import path, include
from .views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register(r'user', UserViewSet)
router.register(r'blog', BlogViewSet)

urlpatterns = [
    path('', include(router.urls)),
]