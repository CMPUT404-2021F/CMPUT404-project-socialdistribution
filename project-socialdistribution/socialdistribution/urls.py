from django.urls import path, include

from .views import IndexView, SignUpView
from .views import dashboard, profile, inbox



urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('dashboard/', dashboard, name='dashboard'),
    path('profile/', profile, name='profile'),
    path('inbox/', inbox, name='inbox'),
    path('posts/', include("post.urls", namespace = 'post')),
]