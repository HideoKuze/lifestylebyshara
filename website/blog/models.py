# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.

class Post(models.Model):
	author = models.ForeignKey(User)
	#blank needs to be set to true so user can edit the title or text of the post without having always edit both
	title = models.CharField(max_length=100, blank=True)
	text = models.TextField(blank=True)
	created_date = models.DateTimeField(default=timezone.now)
	published_date = models.DateTimeField(blank=True, null=True)

	def publish(self):
		self.published_date = timezone.now()
		self.save()

	def __str__(self):
		return self.title