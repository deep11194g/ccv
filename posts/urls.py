from django.conf.urls import url
from posts.serializers import PostListView
from posts import views

urlpatterns = [
    url('bulk-create/', views.bulk_create, name='bulk post create'),
    url('', PostListView.as_view(), name='list all post'),
]