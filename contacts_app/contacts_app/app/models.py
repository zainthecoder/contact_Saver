# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserProfileInfo(models.Model):

	user = models.OneToOneField(User)

	contact_number = models.IntegerField(blank=False)

	def __str__(self):
		return self.user.username


class ContactsInfo(models.Model):
	
	name = models.CharField(max_length=128)
	contact_entry=models.IntegerField(blank=True)
	username = models.CharField(max_length=128, blank=False)

	def __str__(self):
		return self.username