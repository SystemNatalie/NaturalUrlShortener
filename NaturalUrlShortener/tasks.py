from celery import shared_task
from .utils import wipe_old_short_urls

@shared_task
def wipe_old():             # Just a wrapper
    wipe_old_short_urls()
