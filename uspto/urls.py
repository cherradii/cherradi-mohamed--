from django.conf.urls import url

# from . import views

from uspto import views

# urlpatterns = [
#     url(r'^$', views.PollView.as_view()),
# ]

app_name = "uspto"
urlpatterns = [
    # url(r'^$', views.index, name='index'),
    # url(r'^pollView$', views.PollView.as_view()),
    # url(r'^show/$', views.show, name='show'),
    # url(r'^searchShow/$', views.searchShow, name='searchShow'),
    url(r'^$', views.index, name='index'),
    url(r'^show/$', views.show, name='show'),

]

