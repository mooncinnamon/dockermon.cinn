from __future__ import absolute_import

import os

from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'monitoring.settings')

from django.conf import settings

# set the default Django settings module for the 'celery' program.

app = Celery('monitoring',)  # 여기서 ggg는 task를 포함하는 app이름이 되겠습니다.

app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()


@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))
