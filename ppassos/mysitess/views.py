from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView, ListView, DeleteView, UpdateView
from ppassos.models import Contatos


class IndexTemplateView(TemplateView):
    template_name = "mysitess/index.html"

class FormTemplateView(CreateView):
    template_name = "mysitess/contato_form.html"
    model = Contatos
    fields = ('nome', 'telefone_fixo', 'telefone_celular', 'email', 'descricao')
    success_url = reverse_lazy("mysitess:lista_contatos")

class ContatoListView(ListView):
    template_name = "mysitess/lista.html"
    model = Contatos
    context_object_name = "contatos"

class ContatoDeleteView(DeleteView):
    template_name = "mysitess/exclui.html"
    model = Contatos
    context_object_name = 'contato'
    success_url = reverse_lazy("mysitess:lista_contatos")

class ContatoUpdateView(UpdateView):
    template_name = "mysitess/atualiza.html"
    model = Contatos
    fields = '__all__'
    context_object_name = 'contato'
    success_url = reverse_lazy("mysitess:lista_contatos")