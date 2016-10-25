from __future__ import unicode_literals
from ..loginreg.models import User
from django.db import models

# Create your models here.
class LanguageManager(models.Manager):
    def validate_language(self, **kwargs):
        message_list = []
        if len(kwargs['name']) < 2:
            message_list.append("Language name must be at least 2 characters")
            return (False, message_list)
        else:
            message_list.append("Language saved successfully")
            self.create(name=kwargs['name'])
            return (True, message_list)

class Language(models.Model):
    name = models.CharField(max_length=16)
    users = models.ManyToManyField(User)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = LanguageManager()
