# Generated by Django 4.0.5 on 2022-06-17 01:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='data_alteracao',
            field=models.DateField(auto_now=True, verbose_name='Data de Alteração'),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='data_inclusao',
            field=models.DateField(auto_now_add=True, verbose_name='Data de Inclusão'),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='hora_alteracao',
            field=models.DateTimeField(auto_now=True, verbose_name='Hora de Alteração'),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='hora_inclusao',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Hora de Inclusão'),
        ),
        migrations.AlterField(
            model_name='historicalcliente',
            name='data_alteracao',
            field=models.DateField(blank=True, editable=False, verbose_name='Data de Alteração'),
        ),
        migrations.AlterField(
            model_name='historicalcliente',
            name='data_inclusao',
            field=models.DateField(blank=True, editable=False, verbose_name='Data de Inclusão'),
        ),
        migrations.AlterField(
            model_name='historicalcliente',
            name='hora_alteracao',
            field=models.DateTimeField(blank=True, editable=False, verbose_name='Hora de Alteração'),
        ),
        migrations.AlterField(
            model_name='historicalcliente',
            name='hora_inclusao',
            field=models.DateTimeField(blank=True, editable=False, verbose_name='Hora de Inclusão'),
        ),
    ]