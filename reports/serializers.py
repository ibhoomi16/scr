from rest_framework import serializers
from .models import Subscription, ReportHistory

class SubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscription
        fields = '__all__'

class ReportHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ReportHistory
        fields = '__all__'
