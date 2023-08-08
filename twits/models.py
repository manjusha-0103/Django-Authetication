from django.db import models

# Create your models here.

class Twits(models.Model):
    #id = models.BigAutoField(primary_key = True)
    content = models.TextField(blank = True,null = True)
    image = models.FileField(upload_to = 'images/',blank = True,null = True)

    def __str__(self):
        return f"{self.content}"



