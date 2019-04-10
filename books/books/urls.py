"""books URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path

from django.conf.urls import patterns, url, include
from rest_framework.urlpatterns import format_suffix_patterns
from books.views import UserList, UserDetail, GroupList, GroupDetail

urlpatterns = patterns('books.views',
    url(r'^$', 'api_root'),
    url(r'^users/$', UserList.as_view(), name='user-list'),
    url(r'^users/(?P<pk>\d+)/$', UserDetail.as_view(), name='user-detail'),
    url(r'^groups/$', GroupList.as_view(), name='group-list'),
    url(r'^groups/(?P<pk>\d+)/$', GroupDetail.as_view(), name='group-detail'),
)

# Format suffixes
urlpatterns = format_suffix_patterns(urlpatterns, allowed=['json', 'api'])

urlpatterns = [
    path('sort_books/', include('sort_books.urls')),
    path('admin/', admin.site.urls),
    patterns(url(r'^api-auth', include('rest_framework.urls', namespace = 'books')))
]