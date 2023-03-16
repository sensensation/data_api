from django.urls import path
from rest_framework.routers import Route, SimpleRouter
from .views import PingPongView

urlpatterns = [
    path(
        'ping-pong/',
        PingPongView.as_view(),
    )
]
