from django.http import JsonResponse
from .models import Post


def index(request):
    """Controller function for home page"""
    # Always show list of recently created notes on top
    posts = Post.objects.all().order_by('post_id')
    return JsonResponse(posts)
