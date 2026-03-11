from django.contrib import admin
from.models import Review
# Register your models here.
@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('restaurant', 'rating', 'comment', 'created_at')
    search_fields = ('restaurant__name', 'comment')