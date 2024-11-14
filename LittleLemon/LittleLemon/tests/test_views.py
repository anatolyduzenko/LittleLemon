from django.test import TestCase
from Restaurant.models import Menu
from Restaurant.serializers import MenuItemSerializer
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status

class MenuViewTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.item1 = Menu.objects.create(Title="Pizza", Price=12, Inventory=5)
        self.item2 = Menu.objects.create(Title="Burger", Price=6, Inventory=20)
        self.item3 = Menu.objects.create(Title="Pasta", Price=10, Inventory=6)

    def test_get_all(self):
        response = self.client.get(reverse('menu')) 
        menu_items = Menu.objects.all()
        serializer = MenuItemSerializer(menu_items, many=True)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)
