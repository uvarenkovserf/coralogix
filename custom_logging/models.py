from django.db import models
from jsonfield import JSONField


class LogsBuffer(models.Model):
    log = JSONField(default=[])
    level = models.CharField(max_length=255, unique=True)
