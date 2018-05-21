# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django import forms
from .models import Post, ImageUpload

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text',)
        widgets = {
            'myfield': forms.TextInput(attrs={'class': 'myfieldclass'}),
        }

class ImageForm(forms.ModelForm):
	class meta:
		model = ImageUpload