from django.urls import path
from mysitess.views import IndexTemplateView, FormTemplateView, ContatoListView, ContatoDeleteView, ContatoUpdateView
    #CadastroTemplateView, LoginTemplateView

app_name = 'mysitess'

urlpatterns = [

# GET /
    path('', IndexTemplateView.as_view(), name="index"),

    # GET /contato/cadastrar
    path('contato/cadastrar', FormTemplateView.as_view(), name="cadastra_contato"),

    # GET /contatos
    path('contatos/', ContatoListView.as_view(), name="lista_contatos"),

    # GET/POST /funcionarios/excluir/{pk}
    path('contato/excluir/<pk>', ContatoDeleteView.as_view(), name="deleta_contato"),

    # GET/POST /funcionario/{pk}
    path('contato/<pk>', ContatoUpdateView.as_view(), name="atualiza_contato"),
]
