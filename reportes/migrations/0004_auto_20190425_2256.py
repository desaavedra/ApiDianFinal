# Generated by Django 2.2 on 2019-04-25 22:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reportes', '0003_auto_20190425_2255'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reporte',
            name='informacion',
            field=models.CharField(default='No hay informacion', max_length=10485759),
        ),
    ]
