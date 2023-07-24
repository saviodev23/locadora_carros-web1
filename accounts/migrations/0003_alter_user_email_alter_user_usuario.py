# Generated by Django 4.2.3 on 2023-07-20 11:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_user_usuario'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.CharField(blank=True, max_length=100, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='usuario',
            field=models.CharField(max_length=30, unique=True),
        ),
    ]