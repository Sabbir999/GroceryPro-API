#!/bin/sh

# Exit on error
set -e

echo "Waiting for PostgreSQL..."
while ! nc -z db 5432; do
  sleep 0.1
done
echo "PostgreSQL started"

# Run migrations
echo "Running migrations..."
python manage.py migrate --noinput

# Collect static files
echo "Collecting static files..."
python manage.py collectstatic --noinput --clear

# Create superuser if it doesn't exist
if [ "${DJANGO_CREATE_SUPERUSER:-false}" = "true" ]; then
  echo "Creating superuser..."
  python manage.py shell << END
from django.contrib.auth import get_user_model
import os

User = get_user_model()
superuser_username = os.getenv("DJANGO_SUPERUSER_USERNAME")
superuser_email = os.getenv("DJANGO_SUPERUSER_EMAIL")
superuser_password = os.getenv("DJANGO_SUPERUSER_PASSWORD")

if not User.objects.filter(username=superuser_username).exists():
    User.objects.create_superuser(
        superuser_username,
        superuser_email,
        superuser_password,
    )
    print("Superuser created")
END
fi

# Execute the main command
exec "$@"