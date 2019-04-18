# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from django.utils import timezone
from .models import Post
from .forms import PostForm
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect

def index(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = User.objects.get(username='admin')
            post.published_date = timezone.now()
            post.save()
            return HttpResponseRedirect('/')

    else:
        form = PostForm()
    posts = Post.objects.all()
    return render(request, 'microblog/index.html', {'form': form, 'posts': posts})

