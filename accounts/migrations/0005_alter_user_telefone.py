# Generated by Django 4.2.3 on 2023-07-28 18:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_rename_usuario_user_username_alter_user_nome'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='telefone',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]