from restaurants.models import Restaurant
import math

class RestaurantService:
    @staticmethod
    def get_all_restaurants():
        return Restaurant.objects.all()

    @staticmethod
    def get_restaurant_by_id(restaurant_id):
        try:
            return Restaurant.objects.get(id=restaurant_id)
        except Restaurant.DoesNotExist:
            return None

    @staticmethod
    def get_nearby_restaurants(user_lat, user_lng, radius=5):

        restaurants = Restaurant.objects.all()
        nearby = []

        for r in restaurants:

            distance = RestaurantService.calculate_distance(
                user_lat,
                user_lng,
                r.latitude,
                r.longitude
            )

            if distance <= radius:
                r.distance = round(distance, 2)
                nearby.append(r)

        nearby.sort(key=lambda x: x.distance)

        return nearby


    @staticmethod
    def calculate_distance(lat1, lon1, lat2, lon2):

        R = 6371  # Earth radius km

        dlat = math.radians(lat2 - lat1)
        dlon = math.radians(lon2 - lon1)

        a = (
            math.sin(dlat / 2) ** 2
            + math.cos(math.radians(lat1))
            * math.cos(math.radians(lat2))
            * math.sin(dlon / 2) ** 2
        )

        c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

        return R * c
    @staticmethod
    def create_restaurant(data):
        return Restaurant.objects.create(**data)

    @staticmethod
    def update_restaurant(restaurant, data):
        for key, value in data.items():
            setattr(restaurant, key, value)
        restaurant.save()
        return restaurant

    @staticmethod
    def delete_restaurant(restaurant):
        restaurant.delete()
