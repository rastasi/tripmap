#!/bin/bash
set -e

echo "Varok az adatbazisra..."
while ! python -c "
import os, sys, psycopg2
try:
    psycopg2.connect(
        host=os.getenv('DB_HOST', 'db'),
        dbname=os.getenv('DB_NAME', 'djangomap'),
        user=os.getenv('DB_USER', 'djangomap'),
        password=os.getenv('DB_PASSWORD', 'djangomap'),
        port=os.getenv('DB_PORT', '5432')
    ).close()
    sys.exit(0)
except Exception:
    sys.exit(1)
"; do
    echo "  Az adatbazis meg nem kesz, varok 2 masodpercet..."
    sleep 2
done

echo "Adatbazis kesz!"
python manage.py makemigrations --noinput
python manage.py migrate --noinput

# Superuser létrehozása, ha még nem létezik
python manage.py shell -c "
from django.contrib.auth import get_user_model
User = get_user_model()
if not User.objects.filter(username='admin').exists():
    User.objects.create_superuser('admin', 'admin@example.com', 'admin')
    print('Superuser letrehozva: admin / admin')
else:
    print('Superuser mar letezik.')
"

exec python manage.py runserver 0.0.0.0:8000
