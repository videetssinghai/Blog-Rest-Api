from django.conf.urls import url
from django.contrib import admin

from .views import (
UserCreateApiVIew

)

urlpatterns = [
    url(r'^register/$', UserCreateApiVIew.as_view(), name='list'),
    # url(r'^(?P<pk>\d+)/$', CommentDetailAPIView.as_view(), name='detail'),

]
