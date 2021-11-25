from django.urls import path, include

from .views import IndexView
from .views import dashboard, profile, inbox



urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('dashboard/', dashboard, name='dashboard'),
    path('profile/', profile, name='profile'),
    path('inbox/', inbox, name='inbox'),
    path('posts/', include("post.urls", namespace = 'post')),
]