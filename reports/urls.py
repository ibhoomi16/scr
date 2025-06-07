from django.urls import path
from . import views

urlpatterns = [
    path('subscribe/', views.subscribe),
    path('unsubscribe/', views.unsubscribe),
    path('subscriptions/', views.list_subscriptions),
    path('report-history/', views.report_history),
]
