"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from django.views.generic.base import TemplateView
from users import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path(r'^polls/', include('polls.urls', namespace='polls')),
    path(r'^uspto/', include('uspto.urls', namespace='uspto')),
    path(r'^smarts/', include('smarts.urls', namespace='smarts')),
    path(r'^covid/', include('covid.urls', namespace='covid')),
    path(r'^bigs/', include('bigs.urls', namespace='bigs')),
    path(r'^vehicules/', include('vehicules.urls', namespace='vehicules')),
    path(r'^energies/', include('energies.urls', namespace='energies')),
    path(r'^travaux/', include('travaux.urls', namespace='travaux')),
    path(r'^marketing/', include('marketing.urls', namespace='marketing')),
    path('users/', include('users.urls')),
    path('users/', include('django.contrib.auth.urls')),
    path('search/', TemplateView.as_view(template_name='users/search.html'), name='search'),
    path('register/', TemplateView.as_view(template_name='users/register.html'), name='register'),
    path('explorer/', TemplateView.as_view(template_name='users/explorer.html'), name='explorer'),
    path('viz/', TemplateView.as_view(template_name='polls/viz.html'), name='viz'),
    path('autonomousVehicule/', TemplateView.as_view(template_name='polls/autonomousVehicule.html'), name='autonomousVehicule'),
    path('smartCities/', TemplateView.as_view(template_name='polls/smartCities.html'), name='smartCities'),
    path('bigData/', TemplateView.as_view(template_name='polls/bigData.html'), name='bigData'),
    path('renewableEnergy/', TemplateView.as_view(template_name='polls/renewableEnergy.html'), name='renewableEnergy'),
    path('vizuspto/', TemplateView.as_view(template_name='polls/viz.html'), name='viz'),
    path('visualizeUspto/', TemplateView.as_view(template_name='polls/vizualize.html'), name='vizualize'),
    # path('searchUspto/', views.searchUspto, name='searchUSPTO'),
    # path('searchSmartCities/', views.searchUspto, name='searchSmartCities'),
    path('', include('pages.urls')),
    path('getfiles/', views.getfiles, name='getfiles'),
]
