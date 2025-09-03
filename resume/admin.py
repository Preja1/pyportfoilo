from django.contrib import admin

# Register your models here.
from .models import Experience, Education, Skill, Language

admin.site.register(Experience)
admin.site.register(Education)
admin.site.register(Skill)
admin.site.register(Language)