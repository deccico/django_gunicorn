from django.db import models

class Class(models.Model):
    topic = models.CharField(max_length=200)
    class_date = models.DateTimeField('Class date')
    
    def __unicode__(self):
        return self.topic
