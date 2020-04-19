from django.contrib.auth.models import User
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    UpdateView,
    DeleteView,
    CreateView,
)
from .models import Documento


class DocumentosList(ListView):
    model = Documento
"""
    def get_queryset(self):
        funcionario_logada = self.request.user.funcionario.empresa
        return Departamento.objects.filter(empresa=empresa_logada)
"""

class DocumentoEdit(UpdateView):
    model = Documento
    fields = ['descricao']

class DocumentoDelete(DeleteView):
    model = Documento
    success_url = reverse_lazy('list_documentos')

class DocumentoCreate(CreateView):
    model = Documento
    fields = ['descricao','arquivo']

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        form.instance.pertence_id = self.kwargs['funcionario_id']

        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)
