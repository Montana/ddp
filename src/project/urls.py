"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
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
from django.conf import settings
from django.views.generic import View
from django.http import HttpResponse

project_name = getattr(settings, 'PROJECT_DISPLAY_NAME', 'Django')

admin.site.site_header = '%s Admin' % project_name
admin.site.index_title = '%s administration' % project_name
admin.site.site_title = '%s Admin' % project_name

admin.autodiscover()


class IndexView(View):

    def get(self, request, *args, **kwargs):
        return HttpResponse('<h1>%s</h1>' % project_name)


urlpatterns = [
    url(r'^$', IndexView.as_view(), name='index'),
    url(r'^admin/', admin.site.urls),
]
