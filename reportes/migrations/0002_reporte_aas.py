# Generated by Django 2.2 on 2019-04-26 00:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reportes', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='reporte',
            name='aas',
            field=models.CharField(default='pureba', max_length=200),
        ),
    ]