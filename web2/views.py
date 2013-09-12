# Create your views here.
from django.views.generic import DetailView

from models import Pagina, Menu

class PaginaView(DetailView):
    template_name = 'pagina.html'
    model = Pagina

    def get_context_data(self, **kwargs):
        context = super(PaginaView, self).get_context_data(**kwargs)
        context['menus'] = Menu.objects.all()
        return context