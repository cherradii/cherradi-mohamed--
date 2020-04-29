from django.conf.urls import url

# from . import views

from polls import views
from bigs import views

# urlpatterns = [
#     url(r'^$', views.PollView.as_view()),
# ]

app_name = "bigs"
urlpatterns = [
    # url(r'^bigView$', views.BigView.as_view()),
    # url(r'^show/$', views.show, name='show'),
    url(r'^show/$', views.show, name='show'),

]

