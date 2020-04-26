from django.urls import path
from .views import (
   HoraExtraList,
   HoraExtraEdit,
   HoraExtraEditBase,
   HoraExtraDelete,
   HoraExtraCreate,
   UtilizouHoraExtra,
   HoraExtraFuncionario,
   LiberarHoraExtra,
   ExportarParaCSV,
)


urlpatterns = [
   path('', HoraExtraList.as_view(), name='list_hora_extra'),
   path('novo/', HoraExtraCreate.as_view(), name='create_hora_extra'),
   path('novo-funcionario/<int:funcionario_id>/', HoraExtraFuncionario.as_view(), name='create_hora_extra_funcionario'),
   path('editar-funcionario/<int:pk>', HoraExtraEdit.as_view(), name='update_hora_extra'),
   path('editar/<int:pk>', HoraExtraEditBase.as_view(), name='update_hora_extra_base'),
   path('utilizou-hora-extra/<int:pk>', UtilizouHoraExtra.as_view(), name='utilizou_hora_extra'),
   path('liberar-hora-extra/<int:pk>', LiberarHoraExtra.as_view(), name='liberar-hora-extra'),
   path('deleter/<int:pk>', HoraExtraDelete.as_view(), name='delete_hora_extra'),
   path('exportar-csv', ExportarParaCSV.as_view(), name='exportar_csv'),
]