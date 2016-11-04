"""UegProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin

from UegProject import Communication

communication = Communication.Communication()

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', communication.home, name='home'),
    url(r'^load$', communication.sendData, name='load'),
    url(r'^results/$', communication.recieveData, name='results'),
    url(r'^candidate/(?P<candidate_name>\w*)/photo$', communication.candidatePhoto, name='photo'),
    url(r'^voters/(?P<voter_name>\w*)/photo$', communication.voterPhoto, name='photo'),
    url(r'^ascertainment/$', communication.ascertainment, name='ascertainment'),
]
