from django.db import models

# Create your models here.

class Pictures(models.Model):
   
    name = models.CharField(max_length=25)
    pic = models.ImageField(null=True, blank=True, upload_to='static/images')

    def serialize(self):
        return {
            "name":self.name
        }

class MyCV(models.Model):
       
       title = models.CharField(max_length=30)
       mycv = models.FileField(upload_to='static/images')

       def serialize(self):
           return {
                "title":self.title
            }