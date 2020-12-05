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
    url(r'^results/generate/true/(?P<ss>[a-z]+)$', TrueResultsProcessView.as_view()),
    url(r'^results/generate/false/(?P<ss>[a-z]+)$', FalseResultsProcessView.as_view()),
    url(r'^plots/show/(?P<ss>[a-z]+)$', CreatePlotsView.as_view()),
    url(r'^plots/heat/(?P<ss>[a-z]+)$', HeatMapView.as_view()),
    url(r'^plots/marker/(?P<ss>[a-z]+)$', MarkersView.as_view()),
    url(r'^plots/list/(?P<ss>[a-z]+)$', GetListView.as_view()),
    url(r'^plots/some/(?P<ss>[a-z]+)$', SomePlotView.as_view()),
]
