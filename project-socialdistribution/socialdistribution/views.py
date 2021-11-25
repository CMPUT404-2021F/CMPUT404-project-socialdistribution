from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView
from django.contrib.auth.decorators import login_required

from .forms import CustomUserCreationForm

# Create your views here.
class IndexView(TemplateView):
    template_name = "socialdistribution/index.html"

class SignUpView(CreateView):
    # https://learndjango.com/tutorials/django-signup-tutorial
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'




@login_required
def dashboard(request):
    template_name = "socialdistribution/dashboard.html"
    context = {'current_user': request.user}
    return render(request, template_name, context)


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