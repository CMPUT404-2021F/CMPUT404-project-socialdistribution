from django.shortcuts import render

# Create your views here.

from .forms import CustomUserCreationForm
from django.urls import reverse_lazy
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView

# Create your views here.
class IndexView(TemplateView):
    template_name = "socialdistribution/index.html"

class SignUpView(CreateView):
    # https://learndjango.com/tutorials/django-signup-tutorial
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'