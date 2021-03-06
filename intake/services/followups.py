import datetime
from django.db.models import Q
from intake import models, utils
from intake.notifications import slack_simple
from intake.service_objects import FollowupNotification


def get_submissions_due_for_follow_ups(after_id=None):
    """
    Pulls in submissions that are over a month old
    and which have not been sent followups
    """
    today = utils.get_todays_date()
    thirty_days = datetime.timedelta(days=30)
    a_month_ago = today - thirty_days
    end_date_criteria = a_month_ago
    date_criteria = Q(date_received__lte=end_date_criteria)
    if after_id:
        lower_bound = models.FormSubmission.objects.get(
            id=after_id).date_received
        start_date_criteria = Q(date_received__gte=lower_bound)
        date_criteria = date_criteria & start_date_criteria
    exclusion_criteria = ~Q(
        applicant__events__name=models.ApplicationEvent.FOLLOWUP_SENT)
    qset = models.FormSubmission.objects.filter(
        date_criteria & exclusion_criteria
    )
    return qset


def send_followup_notifications(submissions):
    """Sends an email or text via front, based on contact preferences
    """
    notifications = []
    for submission in submissions:
        followup_notification = FollowupNotification(submission)
        followup_notification.send()
        notifications.append(followup_notification)
    return notifications


def send_all_followups_that_are_due(*args, **kwargs):
    submissions = get_submissions_due_for_follow_ups(*args, **kwargs)
    notifications = send_followup_notifications(submissions)
    num_messages = sum([len(n.messages) for n in notifications])
    report_template = str(
        "Sent {} initial followups out of {} applications due for followups")
    report = report_template.format(num_messages, submissions.count())
    slack_simple.send(report)
