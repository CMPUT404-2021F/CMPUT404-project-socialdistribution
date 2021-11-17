from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth.models import Group

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

    # https://stackoverflow.com/questions/60977692/add-user-to-a-group-at-signup-in-django
    def form_valid(self, form):
        user = form.save(commit=False)
        user.save()
        author_group = Group.objects.get(name="author")
        user.groups.add(author_group)
        return super().form_valid(form)

class CreatePostView(generic.CreateView):
    model = Post
    fields = ['title', 'text']
    success_url = "/timeline/"

    # https://stackoverflow.com/questions/19051830/a-better-way-of-setting-values-in-createview
    def form_valid(self, form):
        form.instance.created_by = self.request.user.username
        return super().form_valid(form)

# https://docs.djangoproject.com/en/2.2/topics/class-based-views/intro/#decorating-the-class
@method_decorator(login_required, name="dispatch")
class DashboardView(generic.TemplateView):
    template_name = "socialdistribution/dashboard.html"

    # https://www.valentinog.com/blog/get-context-data/
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["current_user"] = self.request.user
        context["user_fields"] = self.request.user._meta.get_fields()
        return context

# https://docs.djangoproject.com/en/3.2/ref/class-based-views/generic-display/#listview
@method_decorator(login_required, name="dispatch")
class TimelineView(generic.ListView):
    template_name = "socialdistribution/timeline.html"
    model = Post
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["current_user"] = self.request.user
        return context

@method_decorator(login_required, name="dispatch")
class ProfileView(generic.TemplateView):
    template_name = "socialdistribution/profile.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["current_user"] = self.request.user
        return context

@method_decorator(login_required, name="dispatch")
class InboxView(generic.TemplateView):
    template_name = "socialdistribution/inbox.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["current_user"] = self.request.user
        return context