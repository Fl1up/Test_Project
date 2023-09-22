from celery import shared_task

from file.models import File


@shared_task
def file_task(file_id):
    file = File.objects.get(id=file_id)
    file.processed = True
    file.save()