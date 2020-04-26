import csv
import json

from django.contrib.auth.models import User
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import (
    ListView,
    UpdateView,
    DeleteView,
    CreateView,
)
from .forms import RegistroHoraExtraForm
from .models import RegistroHoraExtra


class HoraExtraList(ListView):
    model = RegistroHoraExtra

    def get_queryset(self):
        empresa_logada = self.request.user.funcionario.empresa
        return RegistroHoraExtra.objects.filter(
            funcionario__empresa=empresa_logada
        )


class HoraExtraEdit(UpdateView):
    model = RegistroHoraExtra
    form_class = RegistroHoraExtraForm

    def get_form_kwargs(self):
        kwargs = super(HoraExtraEdit, self).get_form_kwargs()
        kwargs.update({'user': self.request.user})
        return kwargs


class HoraExtraEditBase(UpdateView):
    model = RegistroHoraExtra
    form_class = RegistroHoraExtraForm

    # success_url = reverse_lazy('list_hora_extra')

    def get_success_url(self):
        return reverse_lazy('update_hora_extra_base', args=[self.object.id])

    def get_form_kwargs(self):
        kwargs = super(HoraExtraEditBase, self).get_form_kwargs()
        kwargs.update({'user': self.request.user})
        return kwargs


class HoraExtraDelete(DeleteView):
    model = RegistroHoraExtra
    success_url = reverse_lazy('list_hora_extra')


class HoraExtraCreate(CreateView):
    model = RegistroHoraExtra
    form_class = RegistroHoraExtraForm

    def get_form_kwargs(self):
        kwargs = super(HoraExtraCreate, self).get_form_kwargs()
        kwargs.update({'user': self.request.user})
        return kwargs


class UtilizouHoraExtra(View):
    def post(self, *args, **kwargs):
        registro_hora_extra = RegistroHoraExtra.objects.get(id=kwargs['pk'])
        registro_hora_extra.utilizada = True
        registro_hora_extra.save()

        empregado = self.request.user.funcionario

        response = json.dumps(
            {
                'mensagem': 'Requisição executada',
                'horas': float(empregado.total_horas_extra)
            }
        )
        return HttpResponse(response, content_type='application/json')

class LiberarHoraExtra(View):
    def post(self, *args, **kwargs):
        registro_hora_extra = RegistroHoraExtra.objects.get(id=kwargs['pk'])
        registro_hora_extra.utilizada = False
        registro_hora_extra.save()

        empregado = self.request.user.funcionario

        response = json.dumps(
            {
                'mensagem': 'Requisição executada',
                'horas': float(empregado.total_horas_extra)
            }
        )
        return HttpResponse(response, content_type='application/json')


class HoraExtraFuncionario(CreateView):
    model = RegistroHoraExtra
    fields = ['motivo', 'horas']

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        form.instance.funcionario_id = self.kwargs['funcionario_id']

        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)


class ExportarParaCSV(View):
    def get(self, request):
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachement; filename="somefilename.csv"'

        empresa_logada = self.request.user.funcionario.empresa
        registro_he = RegistroHoraExtra.objects.filter(utilizada=False, funcionario__empresa=empresa_logada)

        writer = csv.writer(response)
        writer.writerow(['id','motivo','funcionario','rest_func','horas','utilizada','empresa'])
        for registro in registro_he:
            writer.writerow([registro.id,
                             registro.motivo,
                             registro.funcionario.nome,
                             registro.funcionario.total_horas_extra,
                             registro.horas,
                             registro.utilizada,
                             registro.funcionario.empresa.nome,
                             ])

        return response
