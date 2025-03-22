#!/bin/bash
set -e

# Migrate database
python manage.py makemigrations --noinput
python manage.py migrate --noinput

# Create admin & court users if they don't exist
python manage.py shell << END
from django.contrib.auth.models import User

if not User.objects.filter(username='admin').exists():
    User.objects.create_superuser('admin', '', 'admin')

for i in range(1, 10):
    username = f'court{i}'
    if not User.objects.filter(username=username).exists():
        User.objects.create_user(username, '', username)
END

# Run your ASGI server
exec daphne -b 0.0.0.0 -p 8000 scoringsys.asgi:application
