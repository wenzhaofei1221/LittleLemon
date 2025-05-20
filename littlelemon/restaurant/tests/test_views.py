from django.test import TestCase
from restaurant.models import Menu
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from restaurant.serializers import menuSerializer

class MenuViewTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        # Create test data
        self.item1 = Menu.objects.create(title="IceCream", price=1.99, inventory=100)
        self.item2 = Menu.objects.create(title="Pizza", price=9.99, inventory=50)
        self.item3 = Menu.objects.create(title="Burger", price=5.49, inventory=75)

    def test_getall(self):
        response = self.client.get(reverse('menu-list')) 

        menu_items = Menu.objects.all()
        serializer = menuSerializer(menu_items, many=True)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)
