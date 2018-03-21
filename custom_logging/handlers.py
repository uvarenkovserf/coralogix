from logging import StreamHandler

BUFFERS = {}


def get_buffer(level):
    if not BUFFERS.get(level):
        from .models import LogsBuffer
        instance, _ = LogsBuffer.objects.get_or_create(level=level)
        BUFFERS[level] = instance

    return BUFFERS[level]


class CustomStreamHandler(StreamHandler):
    def emit(self, record):
        level = record.levelname
        stream_buffer = get_buffer(level)
        log_entry = self.format(record)
        timestamp = record.created
        stream_buffer.log.append((log_entry, timestamp))
        stream_buffer.save()
        super(CustomStreamHandler, self).emit(record)
