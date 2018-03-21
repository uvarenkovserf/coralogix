import logging

from django.http import HttpResponse

logger = logging.getLogger(__name__)


def index(request):
    for name, value in request.COOKIES.items():
        logger.info('{}: {}'.format(name, value))

    return HttpResponse(str(request.COOKIES))
