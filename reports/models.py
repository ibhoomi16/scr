from django.db import models
from django.contrib.auth.models import User

class Subscription(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    pdf = models.BooleanField(default=False)
    html = models.BooleanField(default=False)
    active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.user.username} | {self.start_date} - {self.end_date}"

class ReportHistory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date_sent = models.DateField()
    pdf_sent = models.BooleanField(default=False)
    html_sent = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user.username} | {self.date_sent}"
