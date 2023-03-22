from django.urls import path, re_path
from rest_framework.routers import Route, SimpleRouter

from . import views
from .views import PingPongView
from datatransfer.views import CsvFilesView

urlpatterns = [
    path(
        'ping-pong/', PingPongView.as_view(),
    ),
    re_path(
        r'^file_upload/$', CsvFilesView.as_view(),
    ),
    path(
        'list/', views.PurchaseListAPIView.as_view()
    ),
]
