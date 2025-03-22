import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'scoringsys.settings')
import pytest
from django.test import TestCase
from base.forms import PlayerSelectionForm
from base.models import Player


@pytest.mark.django_db  # ✅ Tells pytest this test needs the DB properly
class PlayerSelectionFormTests(TestCase):
    databases = '__all__'  # ✅ Optional but good for safety

    def test_form_renders_fields(self):
        Player.objects.create(name="Player 1", country="HR", gender="M")
        form = PlayerSelectionForm()
        self.assertIn('player1', form.fields)
        self.assertIn('player2', form.fields)

