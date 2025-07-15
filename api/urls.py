from tracker.views import *
from django.urls import path, include

urlpatterns = [
  
#   project paths
    path('index', get_view),
    path('projects', get_projects),
    path('add_project', add_project),
    path('update_project', update_project),
    path('delete_project', delete_project),

#   tickets path
    path('tickets', get_all_tickets),
    path('add_ticket', create_ticket),
    path('ticket/<id>', ticket),
]
