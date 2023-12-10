from django.urls import path
from .views import MyModelAPIView, SearchView, ExportExcelView


urlpatterns = [
    path('', MyModelAPIView.as_view(), name='car-list-create'),
    path('<int:pk>/', MyModelAPIView.as_view(), name='car-detail'),
    path('search/', SearchView.as_view(), name='car-search'),
    path('export-excel/', ExportExcelView.as_view(), name='export-excel'),

]
