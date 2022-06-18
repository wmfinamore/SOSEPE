# Generated by Django 4.0.5 on 2022-06-17 01:58

from django.db import migrations, models
import django_cpf_cnpj.fields


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0002_alter_cliente_data_alteracao_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='cnpj',
            field=django_cpf_cnpj.fields.CNPJField(blank=True, max_length=18, null=True, verbose_name='CNPJ'),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='cpf',
            field=django_cpf_cnpj.fields.CPFField(blank=True, max_length=14, null=True, verbose_name='CPF'),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='nome',
            field=models.CharField(blank=True, max_length=250, null=True, verbose_name='Nome'),
        ),
        migrations.AlterField(
            model_name='historicalcliente',
            name='cnpj',
            field=django_cpf_cnpj.fields.CNPJField(blank=True, max_length=18, null=True, verbose_name='CNPJ'),
        ),
        migrations.AlterField(
            model_name='historicalcliente',
            name='cpf',
            field=django_cpf_cnpj.fields.CPFField(blank=True, max_length=14, null=True, verbose_name='CPF'),
        ),
        migrations.AlterField(
            model_name='historicalcliente',
            name='nome',
            field=models.CharField(blank=True, max_length=250, null=True, verbose_name='Nome'),
        ),
    ]