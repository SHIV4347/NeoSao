import os
from celery import Celery
from django.conf import settings

# set default settings module
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Cron_project.settings")

# create Celery app
app = Celery("Cron_project")

# load settings with namespace CELERY_
app.config_from_object("django.conf:settings", namespace="CELERY")

# auto-discover tasks in installed apps
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)

# optional: configure a debug logger
@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')
