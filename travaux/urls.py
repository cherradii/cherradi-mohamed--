from django.conf.urls import url

# from . import views

from polls import views
from travaux import views

# urlpatterns = [
#     url(r'^$', views.PollView.as_view()),
# ]

app_name = "travaux"
urlpatterns = [
    # url(r'^travView$', views.TravView.as_view()),
    # url(r'^show/$', views.show, name='show'),
    url(r'^show/$', views.show, name='show'),

]

