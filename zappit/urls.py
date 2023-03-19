"""zappit URL Configuration
"""
from django.contrib import admin
from django.urls import path, include

from posts.views import PostList, PostRetrieveDestroy, VoteCreate

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/posts/',PostList.as_view()),
    path('api/posts/<int:pk>/vote/',VoteCreate.as_view()),
    path('api-auth/',include('rest_framework.urls')),
    path('api/posts/<int:pk>/delete/',PostRetrieveDestroy.as_view()),
]
