import os
import django

# ✅ SETUP first
import pytest

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'scoringsys.settings')
django.setup()

from django.test import TestCase
from django.contrib.admin.sites import AdminSite
from base.admin import BasePlayerAdmin
from base.models import Player

class MockRequest:
    pass

@pytest.mark.django_db
class PlayerAdminTest(TestCase):
    def test_player_admin_str(self):
        player = Player(name="Test Player", country="HR", gender="M")
        admin_obj = BasePlayerAdmin(Player, AdminSite())
        self.assertEqual(str(player), "Test Player (HR)")
