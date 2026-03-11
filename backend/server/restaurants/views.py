from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import RestaurantSerializer
from .services.restaurant_service import RestaurantService


@api_view(['GET'])
def restaurant_list(request):

    restaurants = RestaurantService.get_all_restaurants()

    serializer = RestaurantSerializer(restaurants, many=True)

    return Response(serializer.data)


@api_view(['GET'])
def restaurant_detail(request, pk):

    restaurant = RestaurantService.get_restaurant_by_id(pk)

    if not restaurant:
        return Response(
            {"error": "Restaurant not found"},
            status=status.HTTP_404_NOT_FOUND
        )

    serializer = RestaurantSerializer(restaurant)

    return Response(serializer.data)


@api_view(['GET'])
def nearby_restaurants(request):

    lat = request.GET.get("lat")
    lng = request.GET.get("lng")

    if not lat or not lng:
        return Response({"error": "Latitude and longitude required"})

    restaurants = RestaurantService.get_nearby_restaurants(
        float(lat),
        float(lng)
    )

    serializer = RestaurantSerializer(restaurants, many=True)

    return Response(serializer.data)

@api_view(['POST'])
def restaurant_create(request):

    serializer = RestaurantSerializer(data=request.data)

    if serializer.is_valid():
        restaurant = RestaurantService.create_restaurant(serializer.validated_data)

        return Response(
            RestaurantSerializer(restaurant).data,
            status=status.HTTP_201_CREATED
        )

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT'])
def restaurant_update(request, pk):

    restaurant = RestaurantService.get_restaurant_by_id(pk)

    if not restaurant:
        return Response({"error": "Not found"}, status=404)

    serializer = RestaurantSerializer(restaurant, data=request.data)

    if serializer.is_valid():
        restaurant = RestaurantService.update_restaurant(
            restaurant,
            serializer.validated_data
        )

        return Response(RestaurantSerializer(restaurant).data)

    return Response(serializer.errors, status=400)


@api_view(['DELETE'])
def restaurant_delete(request, pk):

    restaurant = RestaurantService.get_restaurant_by_id(pk)

    if not restaurant:
        return Response({"error": "Not found"}, status=404)

    RestaurantService.delete_restaurant(restaurant)

    return Response({"message": "Restaurant deleted"})
