from django.contrib import admin
from .models import Menu
# Register your models here.
@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    list_display = ('restaurant', 'food_name', 'price', 'category')
    search_fields = ('restaurant__name', 'food_name')