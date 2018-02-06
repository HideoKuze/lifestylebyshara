# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from .models import Post
from django.utils import timezone
from .forms import PostForm
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import redirect
from django.shortcuts import render, get_object_or_404

# Create your views here.

def landing(request):
	return render(request, 'landing.html')

#different page for the blog

def blog(request):
	posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
	return render(request, 'posts.html', {'posts':posts})

def post_detail(request, pk):
	posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')[:7]
	post_detail = get_object_or_404(Post, pk=pk)
	post = get_object_or_404(Post, pk=pk)
	form = PostForm(instance=post)

	if request.method == "POST":
		form = PostForm(request.POST, instance=post)
		if form.is_valid():
			#the new post is saved from the PostForm
			post = form.save(commit=False)
			post.author = request.user
			post.published_date = timezone.now()
			post.save()
			return redirect('post_detail', pk=post.pk)
	else:
		form = PostForm(instance=post)
	return render(request, 'post_detail.html', {'post_detail':post_detail, 'posts': posts, 'form':form })

def new_post(request):
	if request.method == 'POST':
		form = PostForm(request.POST)
		if form.is_valid():
			post = form.save(commit=False)
			post.author = request.user
			post.published_date = timezone.now()
			post.save()
			latest_post = post.id
			#redirect the author to the new post they just created
			return redirect('post_detail', pk=latest_post)

	else:
		form = PostForm()
	return render(request, 'new_post.html', {'form':form})

def post_edit(request, pk):
	post = get_object_or_404(Post, pk=pk)
	if request.method == "POST":
		form = PostForm(request.POST, instance=post)
		if form.is_valid():
			#the new post is saved from the PostForm
			post = form.save(commit=False)
			post.author = request.user
			post.published_date = timezone.now()
			post.save()
			return redirect('post_detail', pk=post.pk)
	else:
		#this displays when the edit button is clicked. Otherwise the if statement is displayed
		form = PostForm(instance=post)

	return render(request, 'blog/new_post.html', {'form': form})