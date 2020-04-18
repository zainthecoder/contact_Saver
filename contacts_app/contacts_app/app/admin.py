# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from app.models import UserProfileInfo ,User,ContactsInfo
# Register your models here.
admin.site.register(UserProfileInfo)
admin.site.register(ContactsInfo)