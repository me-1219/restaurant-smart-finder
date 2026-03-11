from menus.models import Menu


class MenuService:

    @staticmethod
    def get_all_menus():
        return Menu.objects.all()

    @staticmethod
    def get_menu_by_restaurant(restaurant_id):
        return Menu.objects.filter(restaurant_id=restaurant_id)

    @staticmethod
    def get_menu_by_id(menu_id):
        try:
            return Menu.objects.get(id=menu_id)
        except Menu.DoesNotExist:
            return None

    @staticmethod
    def create_menu(data):
        return Menu.objects.create(**data)

    @staticmethod
    def update_menu(menu, data):
        for key, value in data.items():
            setattr(menu, key, value)
        menu.save()
        return menu

    @staticmethod
    def delete_menu(menu):
        menu.delete()
