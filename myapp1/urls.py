from django.conf.urls import url
# 和项目的url配置相似
from myapp1 import views
# 进行url路由的配置时 严格匹配开头和结尾
urlpatterns=[
    #进行url函数设置url路由配置项
    url(r'^blog', views.index),
    url(r"^delete(\d+)",views.delete),
    url(r'^create',views.create),
    url(r'^direct(\d+)',views.direct),
    url(r'^update(\d+)',views.update)
]
handler404 = views.page_not_found