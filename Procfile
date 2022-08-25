release: python manage.py migrate
web: daphne daily_sync.asgi:application
worker: python manage.py runworker -v2 channel_layer