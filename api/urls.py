from tracker.views import get_view
from django.urls import path, include

urlpatterns = [
    path('index/', get_view),
]
