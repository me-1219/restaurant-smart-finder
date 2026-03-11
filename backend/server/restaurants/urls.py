from django.urls import path

from .views import (
    restaurant_list,
    restaurant_detail,
    nearby_restaurants,
    restaurant_create,
    restaurant_update,
    restaurant_delete
)

urlpatterns = [

    path("restaurants/", restaurant_list),
    path("restaurants/<int:pk>/", restaurant_detail),
    path("restaurants/nearby/", nearby_restaurants),
    path("restaurants/create/", restaurant_create),
    path("restaurants/update/<int:pk>/", restaurant_update),
    path("restaurants/delete/<int:pk>/", restaurant_delete),

]
