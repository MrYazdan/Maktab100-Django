from django.db import models
from core.models import TimeStampBaseModel, LogicalBaseModel, StatusMixin


class Post(TimeStampBaseModel, LogicalBaseModel, StatusMixin):
    title = models.CharField(max_length=100)
    content = models.TextField()


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    subject = models.CharField(max_length=100)
    reply_to = models.ForeignKey("self", null=True, on_delete=models.SET_NULL, related_name="replies")