from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'vidascopio.views.home', name='home'),
    url(r'^/?$', TemplateView.as_view(template_name="index.html")),
    url(r'^historia/?$', TemplateView.as_view(template_name="historia.html"), name='historia'),
    url(r'^mision/?$', TemplateView.as_view(template_name="mision.html"), name='mision'),
    url(r'^equipo/?$', TemplateView.as_view(template_name="equipo.html"), name='equipo'),

    url(r'^ninos/?$', TemplateView.as_view(template_name="que_ofrecemos/ninos.html"), name='ninos'),
    url(r'^profesores/?$', TemplateView.as_view(template_name="que_ofrecemos/profesores.html"), name='profesores'),
    url(r'^adultos/?$', TemplateView.as_view(template_name="que_ofrecemos/adultos.html"), name='adultos'),
    url(r'^bibliotecas/?$', TemplateView.as_view(template_name="que_ofrecemos/bibliotecas.html"), name='bibliotecas'),

    url(r'^escribir/?$', TemplateView.as_view(template_name="que_ofrecemos/escribir.html"), name='escribir'),
    url(r'^talleres/?$', TemplateView.as_view(template_name="que_ofrecemos/talleres.html"), name='talleres'),
    url(r'^salidas/?$', TemplateView.as_view(template_name="que_ofrecemos/salidas.html"), name='salidas'),

    url(r'^expresion/?$', TemplateView.as_view(template_name="que_ofrecemos/expresion.html"), name='expresion'),
    url(r'^desafios/?$', TemplateView.as_view(template_name="que_ofrecemos/desafios.html"), name='desafios'),
    url(r'^estrategias/?$', TemplateView.as_view(template_name="que_ofrecemos/estrategias.html"), name='estrategias'),
    url(r'^queleemos/?$', TemplateView.as_view(template_name="que_ofrecemos/queleemos.html"), name='queleemos'),

    url(r'^entrelibros/?$', TemplateView.as_view(template_name="que_ofrecemos/entrelibros.html"), name='entrelibros'),

    url(r'^experiencia/?$', TemplateView.as_view(template_name="compartimos/experiencia.html"), name='experiencia'),
    url(r'^links/?$', TemplateView.as_view(template_name="compartimos/links.html"), name='links'),

    url(r'^contacto/?$', TemplateView.as_view(template_name="contacto.html"), name='contacto'),



)
