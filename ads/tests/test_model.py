from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from ads.models import Profile
from django.core.exceptions import ValidationError
import datetime

# Create your tests here.


class TestPostView(TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_response(self):
        client = Client()
        response = client.get(reverse('ads:index'))
        self.assertEqual(response.status_code, 200)  # сравнение а == b

    def test_birth_date_with_future_data(self):
        with self.assertRaises(ValidationError):
            user = User(
                username='test', first_name='test', last_name='test',
                email='test@test.com'
            )
            user.save()
            Profile.objects.create(user=user)
            user.user_profile.birth_date = datetime.datetime.now() + datetime.timedelta(days=1)
            user.user_profile.save()
