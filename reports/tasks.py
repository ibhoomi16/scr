from datetime import date
from .models import Subscription, ReportHistory
from django.core.mail import EmailMessage
from .utils import generate_pdf
from django.contrib.auth.models import User

def send_daily_reports():
    today = date.today()
    subscriptions = Subscription.objects.filter(active=True, start_date__lte=today, end_date__gte=today)

    for sub in subscriptions:
        user = sub.user

        email = EmailMessage(
            subject="Your Daily Report",
            body=f"Hi {user.username}, here is your daily report for {today}.",
            to=[user.email]  # This will print in terminal using console email backend
        )

        if sub.pdf:
            pdf_file = generate_pdf(str(today))
            email.attach(f"report_{today}.pdf", pdf_file.read(), 'application/pdf')

        email.send()

        # Save to history
        ReportHistory.objects.create(
            user=user,
            date_sent=today,
            pdf_sent=sub.pdf,
            html_sent=sub.html
        )
