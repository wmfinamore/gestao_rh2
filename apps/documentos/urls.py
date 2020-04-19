from django.urls import path
from .views import (
   DocumentosList,
   DocumentoEdit,
   DocumentoDelete,
   DocumentoCreate,
)


urlpatterns = [
   path('', DocumentosList.as_view(), name='list_documentos'),
   path('editar/<int:pk>', DocumentoEdit.as_view(), name='update_documento'),
   path('deleter/<int:pk>', DocumentoDelete.as_view(), name='delete_documento'),
   path('novo/<int:funcionario_id>/', DocumentoCreate.as_view(), name='create_documento'),
]