from celery.decorators import task
from celery.utils.log import get_task_logger
from .emails import send_welcome_email
logger = get_task_logger(__name__)
@task(name="send_welcome_email_task")
def send_welcome_email_task(username,email):
    logger.info("sent welcome email")
    return send_welcome_email(username,email)
