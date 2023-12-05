from django.contrib import admin
from .models import Car


class CarAdmin(admin.ModelAdmin):
    list_display = ('make', 'model', 'year', 'price')
    search_fields = ('make', 'model', 'year')
    list_filter = ('make', 'year')


admin.site.register(Car, CarAdmin)
