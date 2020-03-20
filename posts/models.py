import uuid

from django.db import models


class Post(models.Model):
    post_id = models.CharField(max_length=50, default="rand-{}".format(uuid.uuid4()))
    post_type_id = models.CharField(max_length=10, default="rand")
    parent_id = models.CharField(max_length=10, null=True)
    creation_date = models.DateTimeField(null=True)
    comment_count = models.IntegerField(db_index=True, null=True)
    view_count = models.IntegerField(db_index=True, null=True)
    answer_count = models.IntegerField(db_index=True, null=True)
    score = models.IntegerField(db_index=True, null=True)
    title = models.CharField(max_length=1000, null=True)
    body = models.CharField(max_length=1000, null=True)
    owner_user_id = models.CharField(max_length=10, null=True)
    last_editor_user_id = models.CharField(max_length=10, null=True)
    last_edit_date = models.DateTimeField(null=True)
    last_activity_date = models.DateTimeField(null=True)
    comment_code = models.CharField(max_length=10, default="rand-{}".format(uuid.uuid4()))
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
