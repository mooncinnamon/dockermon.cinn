from __future__ import absolute_import

import os

from celery import Celery
#from celery.signals import worker_shutdown

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'monitoring.settings')

# set the default Django settings module for the 'celery' program.

app = Celery('monitoring')

app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()




@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))
