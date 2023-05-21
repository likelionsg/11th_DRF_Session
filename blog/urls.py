from django.urls import path
from .views import *

urlpatterns = [
    # user urls
    path('user/', UserViewSet.as_view({'get':'list', 'post':'create'})),
    path('user/<int:pk>/', UserViewSet.as_view({'get':'retrieve', 'put':'update','patch':'partial_update','delete':'destroy'})),

    # blog urls
    path('blog/', BlogViewSet.as_view({'get':'list', 'post':'create'})),
    path('blog/<int:pk>/', BlogViewSet.as_view({'get':'retrieve', 'put':'update','patch':'partial_update','delete':'destroy'})),
]