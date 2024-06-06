from django.urls import path
from .views import RegisterView, UserListView, FileListView, FileDetailView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('users/', UserListView.as_view(), name='user-list'),
    path('files/', FileListView.as_view(), name='file-list'),
    # path('login/', FileListView.as_view(), name='file-list'),
    path('files/<int:pk>/', FileDetailView.as_view(), name='file-detail'),
]
