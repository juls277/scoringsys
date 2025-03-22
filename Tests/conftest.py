import pytest
from django.core.management import call_command


@pytest.fixture(scope='session', autouse=True)
def migrate_db(django_db_setup, django_db_blocker):
    """
    Forces a clean DB with migrations for every test session.
    """
    with django_db_blocker.unblock():
        call_command('migrate', verbosity=1)
