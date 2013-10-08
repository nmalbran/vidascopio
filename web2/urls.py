from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView

from web2.views import PaginaView, PaginaSelectView, QueOfrecemosView, ContactoView

urlpatterns = patterns('',
    url(r'^/?$', TemplateView.as_view(template_name="web2/animacion.html")),
    url(r'^inicio/?$', TemplateView.as_view(template_name="web2/inicio.html"), name='inicio'),
    url(r'^historia/?$', TemplateView.as_view(template_name="web2/historia.html"), name='web2.historia'),
    url(r'^equipo/?$', TemplateView.as_view(template_name="web2/equipo.html"), name='web2.equipo'),
    url(r'^experiencia/?$', TemplateView.as_view(template_name="web2/experiencia.html"), name='web2.experiencia'),
    url(r'^links/?$', TemplateView.as_view(template_name="web2/links.html"), name='web2.links'),
    url(r'^que-ofrecemos/?$', QueOfrecemosView.as_view(), name='que_ofrecemos'),

    url(r'^contacto/?$', ContactoView.as_view(), name='web2.contacto'),

    url(r'^pagina/(?P<slug>[-\w0-9]+)/?$', PaginaView.as_view(), name='pagina'),
    url(r'^seccion/(?P<slug>[-\w0-9]+)/?$', PaginaSelectView.as_view(), name='select_pagina'),

)