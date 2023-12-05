# from django.urls import path
# from .views import *
#
# urlpatterns = [
#     path('', MyModelAPIView.as_view()),
#     path('search/', SearchView.as_view()),
# ]

from django.urls import path
from .views import MyModelAPIView, SearchView

urlpatterns = [
    path('', MyModelAPIView.as_view(), name='car-list-create'),
    path('<int:pk>/', MyModelAPIView.as_view(), name='car-detail'),
    path('search/', SearchView.as_view(), name='car-search'),
]
