from django.db import models
from django.contrib.auth import get_user_model
from core.models import TimeStampBaseModel, LogicalBaseModel, StatusMixin


class Post(TimeStampBaseModel, LogicalBaseModel, StatusMixin):
    title = models.CharField(max_length=100)
    content = models.TextField()


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    subject = models.CharField(max_length=100)
    reply_to = models.ForeignKey("self", null=True, on_delete=models.SET_NULL, related_name="replies")


User = get_user_model()


class Content(TimeStampBaseModel):
    title = models.CharField(max_length=200, null=False)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
