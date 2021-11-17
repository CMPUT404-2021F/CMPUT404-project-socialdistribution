from django.urls import path

from . import views

app_name = "socialdistribution"
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('signup/', views.SignUpView.as_view(), name='signup'),
    path('dashboard/', views.DashboardView.as_view(), name='dashboard'),
    path('timeline/', views.TimelineView.as_view(), name='timeline'),
    path('profile/', views.ProfileView.as_view(), name='profile'),
    path('inbox/', views.InboxView.as_view(), name='inbox'),
    path('create-post/', views.CreatePostView.as_view(), name='create-post'),
]