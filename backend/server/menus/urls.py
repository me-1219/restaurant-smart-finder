from django.urls import path

from .views import (
    menu_list,
    menu_by_restaurant,
    menu_create,
    menu_update,
    menu_delete
)

urlpatterns = [

    path("menus/", menu_list),

    path("menus/restaurant/<int:restaurant_id>/", menu_by_restaurant),

    path("menus/create/", menu_create),

    path("menus/update/<int:pk>/", menu_update),

    path("menus/delete/<int:pk>/", menu_delete),

]
