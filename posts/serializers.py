from rest_framework import serializers, generics
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend

from posts.models import Post


# Serializers define the API representation.
class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'


# List view with filter and search
class PostListView(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['score', 'comment_count', 'view_count', 'answer_count', 'parent_id']
    search_fields = ['body', 'title']
    ordering_fields = ['view_count', 'score']
