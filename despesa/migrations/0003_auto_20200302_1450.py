# Generated by Django 3.0.3 on 2020-03-02 17:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('despesa', '0002_auto_20200302_1350'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categoria',
            name='descricao_categoria',
            field=models.CharField(max_length=254, unique=True, verbose_name='categoria'),
        ),
    ]
