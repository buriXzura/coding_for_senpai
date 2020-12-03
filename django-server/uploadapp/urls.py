from django.urls import path
from .views import *
from django.conf.urls import url

urlpatterns = [
    path('upload', FileUploadView.as_view()),
    url(r'^delete/(?P<pk>[0-9]+)$', FileDeleteView.as_view(), name='file-delete'),
    url(r'^list/(?P<ss>[a-z]+)$', FileListView.as_view()),
    url(r'^deleteall/(?P<ss>[a-z]+)$', DeleteAllView.as_view()),
    url(r'^stub/list/(?P<ss>[a-z]+)$', StubListView.as_view()),
    url(r'^stub/delete/(?P<ss>[a-z]+)$', StubFileDeleteView.as_view()),
    url(r'^results/list/(?P<ss>[a-z]+)$', ResultsListView.as_view()),
    url(r'^results/delete/(?P<ss>[a-z]+)$', ResultsFileDeleteView.as_view()),
    url(r'^results/download/(?P<ss>[a-z]+)$', ResultsDownloadView.as_view()),
	
]
