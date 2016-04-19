from django.db import models

class InternalUser(models.Model):
    name = models.CharField(max_length=200, blank=True)
    email = models.EmailField(max_length=255, blank=False, unique=True)
    mobile_number = models.CharField(max_length=11, blank=True)
    password = models.CharField(max_length=255, blank=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.name
