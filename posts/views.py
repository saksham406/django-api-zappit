from rest_framework.exceptions import ValidationError

from rest_framework import generics, permissions, mixins, status
from rest_framework import response

from posts.models import *
from posts.serializers import *
# Create your views here.

class PostList(generics.ListCreateAPIView):
    """API to create post."""
    queryset = Post.objects.filter()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class VoteCreate(generics.CreateAPIView):
    """API to vote."""

    serializer_class = VoteSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):

        user = self.request.user
        post = Post.objects.get(pk=self.kwargs['pk'])

        return Vote.objects.filter(voter=user, post=post)

    def perform_create(self, serializer):

        if self.get_queryset().exists():
            raise ValidationError("Your vote for this post already exists.")
        post = Post.objects.get(pk=self.kwargs['pk'])
        serializer.save(voter=self.request.user, post=post)

    def delete(self, request, *args, **kwargs):
        if self.get_queryset().exists():
            self.get_queryset().delete()
            return response.Response(status= status.HTTP_204_NO_CONTENT)
        raise ValidationError("you never voted for this post.")


class PostRetrieveDestroy(generics.RetrieveDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def delete(self, request, *args, **kwargs):
        post = Post.objects.filter(pk=kwargs['pk'], user=self.request.user)
        if post.exists():
            return self.destroy(request, *args, **kwargs)
        else:
            raise ValidationError('This isn\'t your post to delete, BRUH!')