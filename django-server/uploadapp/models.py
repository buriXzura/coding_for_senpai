from django.db import models

def location(instance, filename):
    l = '{folder}/{name}'.format(folder=instance.session, name=filename)
    return l

class File(models.Model):
    file = models.FileField(blank=False, null=False, upload_to=location)
    session = models.CharField(max_length=20, default='20')
    def __str__(self):
        return self.file.name


