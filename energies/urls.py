from django.conf.urls import url

# from . import views

from polls import views
from energies import views

# urlpatterns = [
#     url(r'^$', views.PollView.as_view()),
# ]

app_name = "energies"
urlpatterns = [
    # url(r'^energyView$', views.EnergyView.as_view()),
    # url(r'^show/$', views.show, name='show'),
    url(r'^show/$', views.show, name='show'),
]

