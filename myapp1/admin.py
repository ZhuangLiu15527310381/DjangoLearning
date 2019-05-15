from django.contrib import admin
from myapp1.models import BlogPost,Comment
# Register your models here.
# 注册模型类
admin.site.register(BlogPost)
admin.site.register(Comment)