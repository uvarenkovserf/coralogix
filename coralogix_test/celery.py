from __future__ import absolute_import, unicode_literals

import os
import sys

from celery import Celery

# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'coralogix_test.settings')

app = Celery('coralogix_test')

# Using a string here means the worker don't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django app configs.
app.autodiscover_tasks()

if "celeryd" in sys.argv:
    DEBUG = False


@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))
