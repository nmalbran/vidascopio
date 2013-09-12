from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView

from web2.views import PaginaView

urlpatterns = patterns('',
    url(r'^/?$', TemplateView.as_view(template_name="inicio.html")),
    url(r'^historia/?$', TemplateView.as_view(template_name="historia.html"), name='historia'),
    url(r'^pagina/?$', TemplateView.as_view(template_name="pagina.html"), name='pagina'),

    url(r'^pagina/(?P<slug>[-\w0-9]+)/?$', PaginaView.as_view(), name='pagina'),

)