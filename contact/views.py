from django.shortcuts import render
from django.views import generic
from contact.models import ContactPage

class ContactPageView(generic.TemplateView):
   template_name='contact.html'

#    def get_context_data(self, **kwargs):
#       data=super().get_context_data(**kwargs)
#       instance=ContactPage.objects.first()
#       data["object"]=instance
#       return data