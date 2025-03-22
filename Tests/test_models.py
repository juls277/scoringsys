import pytest
from base.models import Player, Category

@pytest.mark.django_db
def test_create_player():
    category = Category.objects.create(name="U18")
    player = Player.objects.create(name="Test Player", country="HR", gender="M")
    player.age_categories.add(category)
    assert player.name == "Test Player"
    assert player.country == "HR"
    assert player.gender == "M"
    assert category in player.age_categories.all()
