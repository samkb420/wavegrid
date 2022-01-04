from django.contrib import admin
from .models import Projects, Feedback, Contact, Partners, ProjectImages

# Register your models here.
admin.site.register(Projects)
admin.site.register(Feedback)
admin.site.register(Contact)
admin.site.register(Partners)
admin.site.register(ProjectImages)