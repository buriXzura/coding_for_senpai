from django.urls import path
from .views import *
from django.conf.urls import url

urlpatterns = [
    path('upload', FileUploadView.as_view()),
    url(r'^delete/(?P<pk>[0-9]+)$', FileDeleteView.as_view(), name='file-delete'),
    url(r'^list/(?P<ss>[a-z.@_0-9]+)$', FileListView.as_view()),
    url(r'^deleteall/(?P<ss>[a-z.@_0-9]+)$', DeleteAllView.as_view()),
    url(r'^stub/list/(?P<ss>[a-z.@_0-9]+)$', StubListView.as_view()),
    url(r'^stub/delete/(?P<ss>[a-z.@_0-9]+)$', StubFileDeleteView.as_view()),
    url(r'^results/list/(?P<ss>[a-z.@_0-9]+)$', ResultsListView.as_view()),
    url(r'^results/delete/(?P<ss>[a-z.@_0-9]+)$', ResultsFileDeleteView.as_view()),
    url(r'^results/download/(?P<ss>[a-z.@_0-9]+)$', ResultsDownloadView.as_view()),
    url(r'^results/generate/true/(?P<ss>[a-z.@_0-9]+)$', TrueResultsProcessView.as_view()),
    url(r'^results/generate/false/(?P<ss>[a-z.@_0-9]+)$', FalseResultsProcessView.as_view()),
    url(r'^plots/show/(?P<ss>[a-z.@_0-9]+)$', CreatePlotsView.as_view()),
    url(r'^plots/heat/(?P<ss>[a-z.@_0-9]+)$', HeatMapView.as_view()),
    url(r'^plots/marker/(?P<ss>[a-z.@_0-9]+)$', MarkersView.as_view()),
    url(r'^plots/list/(?P<ss>[a-z.@_0-9]+)$', GetListView.as_view()),
    url(r'^plots/some/(?P<ss>[a-z.@_0-9]+)$', SomePlotView.as_view()),
    url(r'^plots/delete/(?P<ss>[a-z.@_0-9]+)$', DeletePlotsView.as_view()),
]
