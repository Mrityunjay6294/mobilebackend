from django.urls import path


from Groups.views.AuthenticationApi import AuthenticationClass
from Groups.views.MyFeedsApi import MyFeedsApiClass

from Groups.views.MyGroupApi import MygroupApiClass

urlpatterns = [
    path('login/', AuthenticationClass.as_view(),name='Login'),
    path('mycources/', MygroupApiClass.as_view(),name='my_cources'),
    path('myfeeds/', MyFeedsApiClass.as_view(),name='my_feeds'),


    ]