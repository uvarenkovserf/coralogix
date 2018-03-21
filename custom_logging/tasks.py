import requests
import json
from celery import shared_task
from django.conf import settings

from .models import LogsBuffer

LOG_LEVELS = {
    'DEBUG': 1,
    'INFO': 3,
    'WARNING': 4,
    'ERROR': 5,
    'CRITICAL': 6
}


@shared_task
def send_logs_to_coralogix():
    entries = []
    for log_buffer in LogsBuffer.objects.all():
        for entry in log_buffer.log:
            entries.append((log_buffer.level, entry[0], entry[1]))
        log_buffer.log = []
        log_buffer.save()

    body = {
        'privateKey': settings.CORALIGIX_KEY,
        'applicationName': settings.CORALOGIX_APP_NAME,
        'subsystemName': 'TEST',
        'logEntries': [{
            'timestamp': timestamp * 1000,
            'severity': LOG_LEVELS[level],
            'text': text
        } for level, text, timestamp in entries]
    }

    return requests.post(settings.CORALOGIX_ENDPOINT,
                         data=json.dumps(body),
                         headers={'Content-type': 'application/json'})
