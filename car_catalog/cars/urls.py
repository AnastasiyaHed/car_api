# from .views import CarListCreateView, CarDetailView
# from django.urls import path
#
#
# urlpatterns = [
#     path('cars/', CarListCreateView.as_view(), name='car-list-create'),
#     path('cars/<int:pk>/', CarDetailView.as_view(), name='car-detail'),
# ]
#

from django.urls import path
from .views import *

urlpatterns = [
    # path('cars/', CarListCreateView.as_view(), name='car-list-create'),
    # path('cars/<int:pk>/', CarDetailView.as_view(), name='car-detail'),
    # path('cars/<int:pk>/update/', CarUpdateView.as_view(), name='car-update'),
    # path('cars/<int:pk>/delete/', CarDeleteView.as_view(), name='car-delete'),
    path('', MyModelAPIView.as_view()),
    path('search/', SearchView.as_view()),
]

