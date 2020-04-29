from django.conf.urls import url

# from . import views

from polls import views
from vehicules import views

# urlpatterns = [
#     url(r'^$', views.PollView.as_view()),
# ]

app_name = "vehicules"
urlpatterns = [
    # url(r'^vehiculeView$', views.VehiculeView.as_view()),
    # url(r'^show/$', views.show, name='show'),
    url(r'^show/$', views.show, name='show'),

]

