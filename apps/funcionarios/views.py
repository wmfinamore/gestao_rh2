import io

from django.contrib.auth.models import User
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    UpdateView,
    DeleteView,
    CreateView,
)
from reportlab.pdfgen import canvas

from .models import Funcionario


class FuncionariosList(ListView):
    model = Funcionario

    def get_queryset(self):
        empresa_logada = self.request.user.funcionario.empresa
        return Funcionario.objects.filter(empresa=empresa_logada)

class FuncionarioEdit(UpdateView):
    model = Funcionario
    fields = ['nome','departamentos']

class FuncionarioDelete(DeleteView):
    model = Funcionario
    success_url = reverse_lazy('list_funcionarios')

class FuncionarioCreate(CreateView):
    model = Funcionario
    fields = ['nome','departamentos']

    def form_valid(self, form):
        funcionario = form.save(commit=False)
        funcionario.empresa = self.request.user.funcionario.empresa
        funcionario.user = User.objects.create(
            username=funcionario.nome.split(' ')[0]+funcionario.nome.split(' ')[1]
        )
        funcionario.save()
        return super(FuncionarioCreate, self).form_valid(form)


def relatorio_funcionarios(request):
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachement; filename="mypdf.pdf"'

    buffer = io.BytesIO()
    p = canvas.Canvas(buffer)

    p.drawString(200, 810, 'Relatório de Funcionários')

    # palavras = ['palavra1','palavra2','palavra3']
    funcionarios = Funcionario.objects.filter(empresa=request.user.funcionario.empresa)

    str_ = 'Nome: %s | Hora Extra %.2f'

    y = 750
    for funcionario in funcionarios:
        p.drawString(10, y, str_ % (
            funcionario.nome, funcionario.total_horas_extra))
        y -= 20

    p.showPage()
    p.save()

    pdf = buffer.getvalue()
    buffer.close()
    response.write(pdf)

    return response
