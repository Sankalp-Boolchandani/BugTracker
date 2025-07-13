from tracker.views import *
from django.urls import path, include

urlpatterns = [
    path('index/', get_view),
    path('projects/', get_projects),
]
