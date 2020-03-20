from rest_framework import serializers, generics
from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend

from posts.models import Post


# Serializers define the API representation.
class PostSerializer(serializers.Serializer):
    class Meta:
        model = Post
        fields = ('id', 'post_id', 'title', 'body', 'score', 'count')


# List view with filter and search
class PostListView(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ['score', 'body']
    search_fields = ['body', 'title']
