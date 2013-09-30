from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView

from web2.views import PaginaView, PaginaSelectView

urlpatterns = patterns('',
    url(r'^/?$', TemplateView.as_view(template_name="web2/inicio.html")),
    url(r'^historia/?$', TemplateView.as_view(template_name="web2/historia.html"), name='web2.historia'),

    url(r'^pagina/(?P<slug>[-\w0-9]+)/?$', PaginaView.as_view(), name='pagina'),
    url(r'^seccion/(?P<slug>[-\w0-9]+)/?$', PaginaSelectView.as_view(), name='select_pagina'),

)