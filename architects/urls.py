from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('feedback/', feedback, name='feedback'),
    path('wavegridadmin/', admin, name='admin'),
    path('projects/', allProjects, name="all-projects"),
    path('wavegridadmin/partners/',  adminPartners, name="adminpartners"),
   
    path('projects/<int:id>/', project_details, name="project_details"),
    path('update/<int:id>/', updateProject, name='update_project'),
    path('delete-message/<int:id>/', delete_message, name="delete-message"),
    path('delete-project/<int:id>/', delete_project, name="delete-project"),
    path('delete-feedback/<int:id>/', delete_feedback, name="delete-feedback"),
    path('delete-partner/<int:id>/', deletePartner, name="deletePartner"),
]