from django.db import models

class Event(models.Model):
    title=models.CharField(max_length=100)
    description=models.CharField(max_length=250)
    image=models.ImageField(upload_to='event_list/images/')
    date = models.DateField()

    def __str__(self):
        return self.title