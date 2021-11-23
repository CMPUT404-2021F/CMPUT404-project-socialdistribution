from django.http import request
from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

from .forms import CustomUserCreationForm
from .models import Post

# Create your views here.
class IndexView(generic.TemplateView):
    template_name = "socialdistribution/index.html"

class SignUpView(generic.CreateView):
    # https://learndjango.com/tutorials/django-signup-tutorial
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'

class CreatePostView(LoginRequiredMixin, generic.CreateView):
    model = Post
    fields = ['title', 'text']
    success_url = "/timeline/"

    def form_valid(self, form):
        form.instance.created_by = self.request.user.username
        return super().form_valid(form)

class UpdatePostView(LoginRequiredMixin, UserPassesTestMixin, generic.UpdateView):
    model = Post
    fields = ['title', 'text']
    success_url = "/timeline/"

    def form_valid(self, form):
        form.instance.created_by = self.request.user.username
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        return self.request.user.username == post.created_by

class DetailPostView(LoginRequiredMixin, generic.DetailView):
    model = Post

class DeletePostView(LoginRequiredMixin, UserPassesTestMixin, generic.DeleteView):
    model = Post
    success_url = "/timeline/"

    def test_func(self):
        post = self.get_object()
        return self.request.user.username == post.created_by

@login_required
def dashboard(request):
    template_name = "socialdistribution/dashboard.html"
    context = {'current_user': request.user}
    return render(request, template_name, context)

class TimelineListView(LoginRequiredMixin, generic.ListView):
    model = Post
    template_name = "socialdistribution/timeline.html"
    context_object_name = 'posts'
    ordering = ['-date_created']
    paginate_by = 5

    # code inspired by furas from https://stackoverflow.com/questions/69474138/django-cant-get-the-get-response-value-attributeerror-module-django-http-r?noredirect=1&lq=1
    def get_context_data(self, **kwargs):
        if 'size' in self.request.GET:
            self.paginate_by = self.request.GET.get('size', 5)
        
        context = super().get_context_data(**kwargs)
        return context

@login_required
def profile(request):
    template_name = "socialdistribution/profile.html"
    context = {'current_user': request.user}
    return render(request, template_name, context)

@login_required
def inbox(request):
    template_name = "socialdistribution/inbox.html"
    context = {'current_user': request.user}
    return render(request, template_name, context)