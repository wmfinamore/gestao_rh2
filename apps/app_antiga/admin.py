from django.contrib import admin
from .models import Teste, RegistroUsuario


class RegistroUsuariosAdmin(admin.ModelAdmin):
    def get_queryset(self, request):
        return RegistroUsuario.objects.using('antigo').all()


admin.site.register(Teste)
admin.site.register(RegistroUsuario, RegistroUsuariosAdmin)