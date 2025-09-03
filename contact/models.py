from django.db import models

class ContactPage(models.Model):
    Fullname=models.CharField(max_length=50)
    Email_address=models.CharField(max_length=50)
    Phone_number=models.CharField(max_length=10)
    Message=models.TextField()

    def __str__(self):
        return self.Fullname
    
    
