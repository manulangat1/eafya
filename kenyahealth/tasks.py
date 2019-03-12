from celery.decorators import task,periodic_task
from celery.task.schedules import crontab
from celery.utils.log import get_task_logger
from .emails import send_welcome_email,send_history_email
logger = get_task_logger(__name__)
@task(name="send_welcome_email_task")
def send_welcome_email_task(username,email):
    logger.info("sent welcome email")
    return send_welcome_email(username,email)
@periodic_task(run_every=(crontab(minute='*/10')),name="send_history_email")
def send_history_email_task(username,email):
    logger.info("sent history email")
    return send_history_email(username,email)
