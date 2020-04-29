from django.conf.urls import url

# from . import views

from polls import views
from smarts import views

# urlpatterns = [
#     url(r'^$', views.PollView.as_view()),
# ]

app_name = "smarts"
urlpatterns = [
    # url(r'^smartView$', views.SmartView.as_view()),
    # url(r'^show/$', views.show, name='show'),
    url(r'^show/$', views.show, name='show'),

]

