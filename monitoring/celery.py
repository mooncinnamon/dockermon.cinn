from __future__ import absolute_import

import os

from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'monitoring.settings')

from django.conf import settings

# set the default Django settings module for the 'celery' program.

app = Celery('monitoring', broker='django://')  # 여기서 ggg는 task를 포함하는 app이름이 되겠습니다.

# Using a string here means the worker will not have to

# pickle the object when using Windows.

app.config_from_object('django.conf:settings')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)


@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))
