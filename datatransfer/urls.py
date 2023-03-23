from django.urls import path

from . import views
from .views import PingPongView

urlpatterns = [
    path(
        'ping-pong/', PingPongView.as_view(),
    ),
    path(
        'list/', views.PurchaseListAPIView.as_view()
    ),
]
