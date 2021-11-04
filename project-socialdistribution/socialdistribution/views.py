from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.decorators import login_required

from .models import Post

# Create your views here.
class IndexView(generic.TemplateView):
    template_name = "socialdistribution/index.html"

class SignUpView(generic.CreateView):
    # https://learndjango.com/tutorials/django-signup-tutorial
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'

class CreatePostView(generic.CreateView):
    model = Post
    fields = ['title', 'text']
    success_url = "/timeline/"

    def form_valid(self, form):
        form.instance.created_by = self.request.user.username
        return super().form_valid(form)

@login_required
def dashboard(request):
    template_name = "socialdistribution/dashboard.html"
    context = {'current_user': request.user}
    return render(request, template_name, context)

@login_required
def timeline(request):
    template_name = "socialdistribution/timeline.html"
    latest_post_list = Post.objects.order_by('-date_created')[:5]
    context = {'current_user': request.user, 'latest_post_list': latest_post_list}
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