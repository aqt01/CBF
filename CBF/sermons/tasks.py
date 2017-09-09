from __future__ import absolute_import, unicode_literals
from celery import shared_task
from celery.utils.log import get_task_logger
from time import sleep

from CBF.settings.local import DATA_DIR
from CBF.youtube_uploads import fetch_youtube_sermons
from CBF.utils import download_secrets

logger = get_task_logger(__name__)


'''

This tasks populates sermons from youtube

'''

@shared_task(bind=True)
def populate_sermons(self):
    logger.info("Running populate sermon tasks")
    download_secrets() # This method downloads the secrets from s3 for CBF
    fetch_youtube_sermons(DATA_DIR) # imports
