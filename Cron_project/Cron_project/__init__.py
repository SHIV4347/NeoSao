from __future__ import absolute_import, unicode_literals
from Cron_project.celery import app as celery_app  # make sure this matches your project name

# Optional: import tasks if you want them registered immediately
# from . import tasks  

__all__ = ('celery_app',)
