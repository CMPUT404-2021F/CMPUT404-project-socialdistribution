from django.urls import path

from . import views

app_name = "socialdistribution"
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('signup/', views.SignUpView.as_view(), name='signup'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('timeline/', views.TimelineListView.as_view(), name='timeline'),
    path('profile/', views.profile, name='profile'),
    path('inbox/', views.inbox, name='inbox'),
    path('create-post/', views.CreatePostView.as_view(), name='create-post'),
    path('post/<int:pk>/', views.DetailPostView.as_view(), name='post-detail'),
    path('post/<int:pk>/update/', views.UpdatePostView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', views.DeletePostView.as_view(), name='post-delete'),
]