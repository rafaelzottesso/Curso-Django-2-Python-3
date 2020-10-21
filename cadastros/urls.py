from django.urls import path

# Importa as views que a gente criou
from .views import CampusCreate, StatusCreate, SituacaoCreate, ClasseCreate, ProgressaoCreate, CampoCreate, AtividadeCreate, ComprovanteCreate, ValidacaoCreate
from .views import CampusUpdate, ServidorUpdate, StatusUpdate, SituacaoUpdate, ClasseUpdate, ProgressaoUpdate, CampoUpdate, AtividadeUpdate, ComprovanteUpdate, ValidacaoUpdate
from .views import CampusDelete, StatusDelete, SituacaoDelete, ClasseDelete, ProgressaoDelete, CampoDelete, AtividadeDelete, ComprovanteDelete, ValidacaoDelete
from .views import EstadoList, CidadeList, CampusList, StatusList, SituacaoList, ClasseList, ProgressaoList, CampoList, AtividadeList, ComprovanteList, ValidacaoList

# Tem que ser urlpatterns porque é padrão do Django
urlpatterns = [
    path('cadastrar/campus/', CampusCreate.as_view(), name="cadastrar-campus"),
    path('cadastrar/status/', StatusCreate.as_view(), name="cadastrar-status"),
    path('cadastrar/situacao/', SituacaoCreate.as_view(), name="cadastrar-situacao"),
    path('cadastrar/classe/', ClasseCreate.as_view(), name="cadastrar-classe"),
    path('cadastrar/progressao/', ProgressaoCreate.as_view(), name="cadastrar-progressao"),
    path('cadastrar/campo/', CampoCreate.as_view(), name="cadastrar-campo"),
    path('cadastrar/atividade/', AtividadeCreate.as_view(), name="cadastrar-atividade"),
    path('cadastrar/comprovante/', ComprovanteCreate.as_view(), name="cadastrar-comprovante"),
    path('validar/comprovante/<int:id_comprovante>', ValidacaoCreate.as_view(), name="validar-comprovante"),

    path('editar/campus/<int:pk>/', CampusUpdate.as_view(), name="editar-campus"),
    path('editar/status/<int:pk>/', StatusUpdate.as_view(), name="editar-status"),
    path('editar/situacao/<int:pk>/', SituacaoUpdate.as_view(), name="editar-situacao"),
    path('editar/classe/<int:pk>/', ClasseUpdate.as_view(), name="editar-classe"),
    path('editar/progressao/<int:pk>/', ProgressaoUpdate.as_view(), name="editar-progressao"),
    path('editar/campo/<int:pk>/', CampoUpdate.as_view(), name="editar-campo"),
    path('editar/atividade/<int:pk>/', AtividadeUpdate.as_view(), name="editar-atividade"),
    path('editar/comprovante/<int:pk>/', ComprovanteUpdate.as_view(), name="editar-comprovante"),
    path('alterar/validacao/comprovante/<int:id_comprovante>', ValidacaoUpdate.as_view(), name="atualizar-validacao-comprovante"),

    path('excluir/campus/<int:pk>/', CampusDelete.as_view(), name="excluir-campus"),
    path('excluir/status/<int:pk>/', StatusDelete.as_view(), name="excluir-status"),
    path('excluir/situacao/<int:pk>/', SituacaoDelete.as_view(), name="excluir-situacao"),
    path('excluir/classe/<int:pk>/', ClasseDelete.as_view(), name="excluir-classe"),
    path('excluir/progressao/<int:pk>/', ProgressaoDelete.as_view(), name="excluir-progressao"),
    path('excluir/campo/<int:pk>/', CampoDelete.as_view(), name="excluir-campo"),
    path('excluir/atividade/<int:pk>/', AtividadeDelete.as_view(), name="excluir-atividade"),
    path('excluir/comprovante/<int:pk>/', ComprovanteDelete.as_view(), name="excluir-comprovante"),

    path('listar/estados/', EstadoList.as_view(), name="listar-estado"),
    path('listar/cidades/', CidadeList.as_view(), name="listar-cidade"),
    path('listar/campus/', CampusList.as_view(), name="listar-campus"),
    path('listar/status/', StatusList.as_view(), name="listar-status"),
    path('listar/situacoes/', SituacaoList.as_view(), name="listar-situacao"),
    path('listar/classes/', ClasseList.as_view(), name="listar-classe"),
    path('listar/progressoes/', ProgressaoList.as_view(), name="listar-progressao"),
    path('listar/campos/', CampoList.as_view(), name="listar-campo"),
    path('listar/atividades/', AtividadeList.as_view(), name="listar-atividade"),
    path('listar/comprovantes/', ComprovanteList.as_view(), name="listar-comprovante"),

]
