from django.conf.urls import url

# from . import views

from polls import views
from marketing import views

# urlpatterns = [
#     url(r'^$', views.PollView.as_view()),
# ]

app_name = "marketing"
urlpatterns = [
    # url(r'^markView$', views.MarkView.as_view()),
    # url(r'^show/$', views.show, name='show'),
    url(r'^show/$', views.show, name='show'),

]

