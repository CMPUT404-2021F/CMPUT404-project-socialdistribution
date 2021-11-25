from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Post


class PostListView(LoginRequiredMixin, ListView):
    model = Post
    template_name = "post/post_list.html"
    context_object_name = "post_list"

    ordering = ["-date"]

class PostDetailView(LoginRequiredMixin, DetailView):
    model = Post
    template_name = "post/post_detail.html"
    context_object_name = "post"

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    template_name = "post/post_update.html"
    fields = ('title', 'text')
    context_object_name = "post"

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = "post/post_delete.html"
    success_url = reverse_lazy("post:post_list")
    context_object_name = "post"

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    template_name = "post/post_new.html"
    fields = ('title', 'text')
    success_url = reverse_lazy("post:post_list")
    context_object_name = "post"

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
