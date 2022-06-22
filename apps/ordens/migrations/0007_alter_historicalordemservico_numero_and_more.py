# Generated by Django 4.0.5 on 2022-06-22 01:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ordens', '0006_historicalordemservico_status_ordemservico_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historicalordemservico',
            name='numero',
            field=models.PositiveBigIntegerField(blank=True, editable=False, null=True, verbose_name='Número da O.S.'),
        ),
        migrations.AlterField(
            model_name='ordemservico',
            name='numero',
            field=models.PositiveBigIntegerField(blank=True, editable=False, null=True, verbose_name='Número da O.S.'),
        ),
    ]