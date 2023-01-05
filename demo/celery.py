

########  Schedule the tasks than run these commands  #########

# 1. celery -A demo.celery worker --pool=solo -l info
# 2. celery -A demo.celery beat -l INFO
##   celery -A myproject.celery worker --pool=solo -l info
# 3. python3 manage.py runserver
import os
from celery import Celery
from datetime import timedelta
 
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'demo.settings')
app = Celery('demo')
app.config_from_object('django.conf:settings', namespace='CELERY')
 
app.conf.timezone = 'Asia/Kolkata'
 
app.conf.beat_schedule = {
    "every_thirty_seconds": {
        "task": "myapp.tasks.thirty_second_func",
        "schedule": timedelta(seconds=10),
    },
}
 
app.autodiscover_tasks()