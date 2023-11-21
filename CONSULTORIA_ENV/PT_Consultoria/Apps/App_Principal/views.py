from django.views.generic import TemplateView, ListView, CreateView, UpdateView, DeleteView

class InicioTemplateView(TemplateView):
    template_name = "inicio.html"
