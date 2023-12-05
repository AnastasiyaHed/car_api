from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('cars.urls')),
    # path('', include('cars.urls')),
    # path('', RedirectView.as_view(url='api/cars/')),  # Перенаправляем пустой путь на ваш список машин
    # path('', CarListView.as_view(), name='home'),  # Добавляем страницу с списком машин как главную

]
