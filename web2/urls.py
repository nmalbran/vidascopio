from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView


urlpatterns = patterns('',
    url(r'^/?$', TemplateView.as_view(template_name="inicio.html")),
    url(r'^historia/?$', TemplateView.as_view(template_name="historia.html"), name='historia'),


)