# Generated by Django 3.0.5 on 2020-06-27 13:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appWeb', '0010_servidor_usr_srv'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='pwd',
            field=models.CharField(max_length=80, verbose_name='Contraseña'),
        ),
    ]
