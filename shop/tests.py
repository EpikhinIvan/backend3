from django.test import TestCase
from django.contrib.auth.models import User
from .models import UserProfile, Order

class UserProfileModelTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')

    def test_user_profile_creation(self):
        user_profile = UserProfile.objects.create(user=self.user, phone_number='1234567890', address='Taddress')
        self.assertEqual(user_profile.__str__(), 'testuser')

class OrderModelTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.order = Order.objects.create(user=self.user, item='Test Order', special_requests='Test Special Requests')

    def test_order_creation(self):
        self.assertEqual(self.order.__str__(), 'Test Order - testuser')

    def test_order_defaults(self):
        self.assertEqual(self.order.status, 'new')
