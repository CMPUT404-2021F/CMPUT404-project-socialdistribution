from django.urls import path
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView

app_name = "post"
urlpatterns = [
    path('', PostListView.as_view(), name='post_list'),
    path('<int:pk>,', PostDetailView.as_view(), name="post_detail"),
    path('new/', PostCreateView.as_view(), name='post_new'),
    path('<int:pk>/update,', PostUpdateView.as_view(), name="post_update"),
    path('<int:pk>/delete,', PostDeleteView.as_view(), name="post_delete"),
]