from django.shortcuts import render
from django.views import generic
from project.models import Project

class ProjectPageView(generic.TemplateView):
   template_name='projects.html'

#    def get_context_data(self, **kwargs):
#       data=super().get_context_data(**kwargs)
#       instance=Project.objects.first()
#       data["object"]=instance
#       return data