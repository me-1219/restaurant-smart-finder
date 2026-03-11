from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .serializers import MenuSerializer
from .services.menu_service import MenuService


@api_view(['GET'])
def menu_list(request):

    menus = MenuService.get_all_menus()

    serializer = MenuSerializer(menus, many=True)

    return Response(serializer.data)


@api_view(['GET'])
def menu_by_restaurant(request, restaurant_id):

    menus = MenuService.get_menu_by_restaurant(restaurant_id)

    serializer = MenuSerializer(menus, many=True)

    return Response(serializer.data)


@api_view(['POST'])
def menu_create(request):

    serializer = MenuSerializer(data=request.data)

    if serializer.is_valid():

        menu = MenuService.create_menu(serializer.validated_data)

        return Response(
            MenuSerializer(menu).data,
            status=status.HTTP_201_CREATED
        )

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT'])
def menu_update(request, pk):

    menu = MenuService.get_menu_by_id(pk)

    if not menu:
        return Response({"error": "Menu not found"}, status=404)

    serializer = MenuSerializer(menu, data=request.data)

    if serializer.is_valid():

        menu = MenuService.update_menu(menu, serializer.validated_data)

        return Response(MenuSerializer(menu).data)

    return Response(serializer.errors, status=400)


@api_view(['DELETE'])
def menu_delete(request, pk):

    menu = MenuService.get_menu_by_id(pk)

    if not menu:
        return Response({"error": "Menu not found"}, status=404)

    MenuService.delete_menu(menu)

    return Response({"message": "Menu deleted"})
