from django.db import models


class Post(models.Model):
    post_id = models.IntegerField(max_length=10)
    post_type_id = models.IntegerField(max_length=5)
    parent_id = models.IntegerField(max_length=10)
    creation_date = models.DateTimeField()
    score = models.IntegerField(max_length=10)
    body = models.CharField(max_length=1000)
    owner_user_id = models.IntegerField(max_length=10)
    last_editor_user_id = models.IntegerField(max_length=10)
    last_edit_date = models.DateTimeField()
    last_activity_date = models.DateTimeField()
    comment_code = models.IntegerField(max_length=10)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
