#!/bin/bash

# Exit script on any error
set -e

# Apply database migrations
echo "Applying database migrations..."
python manage.py migrate --noinput

# Create superuser if it doesn't exist
echo "Creating superuser if it does not exist..."
python manage.py shell << END
from django.contrib.auth.models import User
if not User.objects.filter(username='admin').exists():
    User.objects.create_superuser('admin', '', 'admin')
END

# Start Daphne ASGI server
echo "Starting Daphne server..."
exec daphne -b 0.0.0.0 -p 8000 scoringsys.asgi:application
