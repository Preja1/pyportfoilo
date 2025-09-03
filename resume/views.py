from django.shortcuts import render
from django.views import generic
from resume.models import Experience
from resume.models import Education
from resume.models import Skill
from resume.models import Language

class ResumePageView(generic.TemplateView):
   template_name='resume.html'

#    def get_context_data(self, **kwargs):
#       data=super().get_context_data(**kwargs)
#       instance=Experience.objects.first()
#       data["object"]=instance
#       return data