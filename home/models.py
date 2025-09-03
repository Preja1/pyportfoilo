from django.db import models
from django.forms import ValidationError

class HomePage(models.Model):
    #Banner Section
    label=models.CharField(max_length=100)
    mini_title=models.CharField(max_length=120)
    main_title=models.CharField(max_length=255)
    Photo=models.ImageField()

    #About section
    about_title=models.CharField(max_length=255)
    about_description=models.TextField()

    def full_clean(self,*args,**kwargs):
        if not self.pk and HomePage.objects.exists():
            raise ValidationError(
                message="Not allowed to create multiple home page(s)"
            )
        super().full_clean(*args,**kwargs)

    def __str__(self):
        return "Home Page Content"