# Generated by Django 5.1.7 on 2025-04-11 19:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('formulario', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nivelaciontierra',
            name='distancia_canaleta',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='nivelaciontierra',
            name='superficie_parcela',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='nivelaciontierra',
            name='tamano_canaleta',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='nivelaciontierra',
            name='tiempo_promedio_riego',
            field=models.FloatField(),
        ),
    ]
