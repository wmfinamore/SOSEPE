# Generated by Django 4.0.5 on 2022-06-17 23:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ordens', '0003_status_pedido'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Status_Pedido',
            new_name='StatusPedido',
        ),
    ]
