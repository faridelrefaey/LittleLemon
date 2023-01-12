from django.test import TestCase
from restaurant.models import Menu, Booking
class MenuTest(TestCase):
    def setUp(self):
        Menu.objects.create(title="IceCream", price=25.50, inventory=5)
        
    def test_get_item(self):
        item = Menu.objects.get(title="IceCream")
        self.assertEqual(item.__str__(), "IceCream : 25.50")

class MenuViewTest(TestCase):
    def setUp(self):
        Menu.objects.create(title="IceCream", price=25.50, inventory=5)
        Menu.objects.create(title="Salad", price=5.50, inventory=3)
        Menu.objects.create(title="Fried Chicken", price=14.50, inventory=2)

    def test_getall(self):
        item1 = Menu.objects.get(title="IceCream")
        item2 = Menu.objects.get(title="Salad")
        item3 = Menu.objects.get(title="Fried Chicken")
        self.assertEqual(item1.__str__(), "IceCream : 25.50")
        self.assertEqual(item2.__str__(), "Salad : 5.50")
        self.assertEqual(item3.__str__(), "Fried Chicken : 14.50")
        print(item3)