from django.urls import reverse
from django.test import Client, TestCase
from base.models import Player, Category
from django.contrib.auth.models import User


class PlayerViewTests(TestCase):
    def setUp(self):
        self.client = Client()
        category = Category.objects.create(name="U18")
        self.player = Player.objects.create(name="Test Player", country="HR", gender="M")
        self.player.age_categories.add(category)

    def test_get_players(self):
        response = self.client.get(reverse('get_players'))
        self.assertContains(response, "Test Player")

    def test_get_players_filter_gender(self):
        response = self.client.get(reverse('get_players'), {'gender': 'M'})
        self.assertContains(response, "Test Player")


class LoginViewTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_superuser('admin', 'admin@test.com', 'password')

    def test_login_admin_redirects_to_admin(self):
        response = self.client.post(reverse('login'), {'username': 'admin', 'password': 'password'})
        self.assertRedirects(response, reverse('admin:index'))
