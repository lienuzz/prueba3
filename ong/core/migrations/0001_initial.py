# Generated by Django 3.2.5 on 2021-07-14 16:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='categoria',
            fields=[
                ('idCategoria', models.IntegerField(primary_key=True, serialize=False, verbose_name='Id de Categoria')),
                ('nombreCategoria', models.CharField(max_length=50, verbose_name='Nombre de la Categoria')),
            ],
        ),
        migrations.CreateModel(
            name='Pintura',
            fields=[
                ('idPintura', models.IntegerField(primary_key=True, serialize=False, verbose_name='IDpintura')),
                ('nombre', models.CharField(max_length=20, verbose_name='Nombre pintura')),
                ('autor', models.CharField(blank=True, max_length=50, null=True, verbose_name='Autor')),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.categoria')),
            ],
        ),
    ]