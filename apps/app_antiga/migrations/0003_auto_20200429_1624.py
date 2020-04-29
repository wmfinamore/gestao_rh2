# Generated by Django 2.2.10 on 2020-04-29 19:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_antiga', '0002_registrousuarios'),
    ]

    operations = [
        migrations.CreateModel(
            name='RegistroUsuario',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=100)),
                ('idade', models.IntegerField()),
                ('salario', models.DecimalField(decimal_places=2, max_digits=7)),
            ],
            options={
                'db_table': 'registro_usuarios',
            },
        ),
        migrations.DeleteModel(
            name='RegistroUsuarios',
        ),
    ]
