# Generated by Django 4.2.3 on 2023-07-22 17:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('locacao', '0004_alter_locacao_hora_devolucao_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='locacao',
            name='data_devolucao',
            field=models.DateField(blank=True, null=True, verbose_name='Data de Devolução'),
        ),
        migrations.AlterField(
            model_name='locacao',
            name='data_locacao',
            field=models.DateField(blank=True, null=True, verbose_name='Data de Locação'),
        ),
    ]