# Create your views here.
import os
from postmark import PMMail
from django.views.generic import DetailView, TemplateView, View
from django.shortcuts import render_to_response, get_object_or_404, redirect
from django.template import RequestContext

from models import Pagina, Menu
from forms import ContactoForm

class PaginaView(DetailView):
    template_name = 'web2/pagina.html'
    model = Pagina

    def get_context_data(self, **kwargs):
        context = super(PaginaView, self).get_context_data(**kwargs)
        context['menus'] = Menu.objects.all()
        return context


class PaginaSelectView(DetailView):
    template_name = 'web2/select_pagina.html'
    model = Menu

    def get_context_data(self, **kwargs):
        context = super(PaginaSelectView, self).get_context_data(**kwargs)
        context['menus'] = Menu.objects.all()
        return context


class QueOfrecemosView(TemplateView):
    template_name = 'web2/que_ofrecemos.html'

    def get_context_data(self, **kwargs):
        context = super(QueOfrecemosView, self).get_context_data(**kwargs)
        context['menus'] = Menu.objects.all()
        return context


class ContactoView(View):
    template_name = 'web2/contacto.html'

    def get(self, request):
        form = ContactoForm()
        return render_to_response(self.template_name, {'form': form}, context_instance=RequestContext(request))

    def post(self, request):
        form = ContactoForm(request.POST)
        if form.is_valid():
            body = """
            Mensaje enviado desde vidascopio.cl

            Nombre: %(nombre)s
            Mail: %(mail)s
            Telefono: %(telefono)s
            Mensaje:
            %(mensaje)s
            """ % form.cleaned_data

            message = PMMail(api_key = os.environ.get('POSTMARK_API_KEY'),
                             subject = "Contacto de '%s' desde Vidascopio.cl" % form.cleaned_data['nombre'],
                             sender = "contacto@vidascopio.cl",
                             to = "nmalbran@gmail.com",
                             text_body = body,
                             tag = "contacto-web")

            enviado = message.send()
            if enviado:
                return render_to_response('web2/contacto_fin.html', context_instance=RequestContext(request))

        return render_to_response(self.template_name, {'form': form}, context_instance=RequestContext(request))