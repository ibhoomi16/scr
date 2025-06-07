from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Subscription, ReportHistory
from .serializers import SubscriptionSerializer, ReportHistorySerializer
from django.contrib.auth.models import User
from datetime import date
from rest_framework import status
import traceback
@api_view(['POST'])
def subscribe(request):
    try:
        # Step 1: Check if a user exists
        user = User.objects.first()
        if not user:
            return Response({'error': 'No user found'}, status=status.HTTP_400_BAD_REQUEST)

        # Step 2: Validate request data
        required_fields = ['start_date', 'end_date', 'pdf', 'html']
        missing = [field for field in required_fields if field not in request.data]
        if missing:
            return Response({'error': f'Missing fields: {", ".join(missing)}'}, status=status.HTTP_400_BAD_REQUEST)

        # Step 3: Create Subscription
        subscription = Subscription.objects.create(
            user=user,
            start_date=request.data['start_date'],
            end_date=request.data['end_date'],
            pdf=request.data['pdf'],
            html=request.data['html'],
            active=True
        )

        return Response({'message': 'Subscribed successfully'})

    except Exception as e:
        # Step 4: Print full traceback in terminal
        print("ERROR TRACEBACK:\n", traceback.format_exc())
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['POST'])
def unsubscribe(request):
    user = User.objects.first()
    Subscription.objects.filter(user=user, active=True).update(active=False)
    return Response({'message': 'Unsubscribed successfully'})

@api_view(['GET'])
def list_subscriptions(request):
    try:
        user = User.objects.first()
        if not user:
            return Response({'error': 'No user found'}, status=status.HTTP_400_BAD_REQUEST)

        subs = Subscription.objects.filter(user=user)
        serializer = SubscriptionSerializer(subs, many=True)
        return Response(serializer.data)

    except Exception as e:
        print("ERROR TRACEBACK:\n", traceback.format_exc())
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
@api_view(['GET'])
def report_history(request):
    user = User.objects.first()
    history = ReportHistory.objects.filter(user=user)
    serializer = ReportHistorySerializer(history, many=True)
    return Response(serializer.data)

