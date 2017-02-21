# -*- coding: utf-8 -*-
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    UpdateView,
    ListView
)

from .models import (
	Post,
)


class PostCreateView(CreateView):

    model = Post


class PostDeleteView(DeleteView):

    model = Post


class PostDetailView(DetailView):

    model = Post


class PostUpdateView(UpdateView):

    model = Post


class PostListView(ListView):

    model = Post

