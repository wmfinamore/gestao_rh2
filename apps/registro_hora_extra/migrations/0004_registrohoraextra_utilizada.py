# Generated by Django 2.2.10 on 2020-04-23 19:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registro_hora_extra', '0003_registrohoraextra_horas'),
    ]

    operations = [
        migrations.AddField(
            model_name='registrohoraextra',
            name='utilizada',
            field=models.BooleanField(default=False),
        ),
    ]