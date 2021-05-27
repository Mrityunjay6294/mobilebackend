from django.urls import path

from Cources.CourseServer.CourseViews.CourseServerCode import SnippetList
from Cources.CourseServer.CourseViews.SampleView import sample

urlpatterns = [

    path('snippets/', SnippetList.as_view(),name='get feeds'),
    path('sample/', sample.as_view(),name='get feeds'),
    ]