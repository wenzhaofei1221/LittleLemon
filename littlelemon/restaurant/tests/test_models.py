from django.test import TestCase
from restaurant.models import Menu

class MenuTest(TestCase):
    def test_get_item(self):
        item = Menu.objects.create(title="IceCream",price=1.99, inventory=100)
        self.assertEqual(str(item),"IceCream:1.99")
        