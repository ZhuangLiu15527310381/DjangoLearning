from django.db import models


# Create your models here.
class BlogPost(models.Model):
    author_name = models.CharField(max_length=32)
    title = models.CharField(max_length=150)
    body = models.TextField()
    timestamp = models.DateTimeField()

class Comment(models.Model):
    comment_dateTime = models.DateTimeField()
    comment_body = models.TextField()
    blogPost = models.ForeignKey('BlogPost',on_delete=models.CASCADE) # 一条Blog对应多个
