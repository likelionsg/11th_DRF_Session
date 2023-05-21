from django.urls import path
from .views import *

urlpatterns = [
    # user urls
    path('create-user/', UserCreateAPIView.as_view()),
    path('list-user/', UserListAPIView.as_view()),
    path('retrieve-user/<int:pk>/', UserRetrieveAPIView.as_view()),
    path('update-user/<int:pk>/', UserUpdateAPIView.as_view()),
    path('destroy-user/<int:pk>/', UserDestroyAPIView.as_view()),

    # blog urls
    path('create-blog/', BlogCreateAPIView.as_view()),
    path('list-blog/', BlogListAPIView.as_view()),
    path('retrieve-blog/<int:pk>/', BlogRetrieveAPIView.as_view()),
    path('update-blog/<int:pk>/', BlogUpdateAPIView.as_view()),
    path('destroy-blog/<int:pk>/',BlogDestroyAPIView.as_view()),
]