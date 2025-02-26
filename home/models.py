# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__
class Doc_Details(models.Model):

    #__Doc_Details_FIELDS__
    record_id = models.CharField(max_length=255, null=True, blank=True)
    record_name = models.CharField(max_length=255, null=True, blank=True)
    record_vendor_name = models.CharField(max_length=255, null=True, blank=True)

    #__Doc_Details_FIELDS__END

    class Meta:
        verbose_name        = _("Doc_Details")
        verbose_name_plural = _("Doc_Details")



#__MODELS__END
