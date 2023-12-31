# Generated by Django 4.2.3 on 2023-08-10 22:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Marca',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.CharField(default='', max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Modelo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.CharField(default='', max_length=20)),
                ('marca', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='automovel.marca')),
            ],
        ),
        migrations.CreateModel(
            name='Automovel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('placa', models.CharField(max_length=10)),
                ('cor', models.CharField(choices=[('Branco', 'Branco'), ('Preto', 'Preto'), ('Prata', 'Prata'), ('Vermelho', 'Vermelho'), ('Azul', 'Azul'), ('Verde', 'Verde'), ('Amarelo', 'Amarelo'), ('Laranja', 'Laranja'), ('Rosa', 'Rosa'), ('Roxo', 'Roxo')], default='Branco', max_length=20)),
                ('nr_portas', models.IntegerField(default=4, verbose_name='Número de portas')),
                ('tipo_combustivel', models.CharField(choices=[('Gasolina', 'Gasolina'), ('Etanol', 'Etanol'), ('Diesel', 'Diesel'), ('Flex', 'Flex'), ('Eletrico', 'Elétrico')], default='Flex', max_length=10)),
                ('quilometragem', models.IntegerField(default=0)),
                ('renavam', models.IntegerField(default=0)),
                ('chassi', models.CharField(default='', max_length=20)),
                ('ano_fabricacao', models.IntegerField(verbose_name='Ano de Fabricação')),
                ('descricao', models.TextField(max_length=300)),
                ('valor_locacao', models.DecimalField(decimal_places=2, max_digits=8, verbose_name='Preço de locação')),
                ('imagem', models.ImageField(null=True, upload_to='images/%Y/%m/%d/')),
                ('disponivel', models.BooleanField()),
                ('modelo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='automovel.modelo')),
            ],
        ),
    ]
