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

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', Communication.teste, name='teste'),
    url(r'^teste/', Communication.teste1, name='teste1'),
    url(r'^teste2/', Communication.teste2, name='teste2'),

    url(r'^teste3/(?P<uev_id>\d+)/$', Communication.teste3, name='teste3'),

    # use this URL to test http://127.0.0.1:8181/teste4/?query=uev&uev_id=12
    url(r'^teste4/$', Communication.teste4, name='teste4'),

    url(r'^carregar/$', Communication.Communication.sendData, name='carregar'),
]
