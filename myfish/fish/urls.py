from django.conf.urls import url
from django.views.generic import TemplateView
from . import views
from django.conf import settings

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^index$', views.index, name='index'),
    url(r'^upload$', views.upload, name='upload'),
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
    url(r'^.*', views.forbidden, name='forbidden')
]