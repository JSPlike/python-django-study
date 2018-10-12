
from django.conf.urls import url
from django.contrib import admin

from blog.views import BlogLV, BlogDV # BlogListView, BlogDetailView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', BlogLV.as_view(), name='index'),

    #Blog app
    url(r'^blog/$', BlogLV.as_view(), name='index'),
    #정규표현식에 관한 내용 숙지필요
    url(r'^blog/(?P<pk>\d+)/$', BlogDV.as_view(), name='detail'),
]


