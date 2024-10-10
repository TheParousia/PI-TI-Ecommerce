# Generated by Django 4.2.16 on 2024-10-09 22:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Marca',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Modelo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Produto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('modelo', models.CharField(max_length=30)),
                ('descricao', models.CharField(max_length=100)),
                ('capacidade1', models.CharField(max_length=10)),
                ('capacidade2', models.CharField(max_length=10)),
                ('capacidade3', models.CharField(max_length=10)),
                ('qtd_estoque', models.IntegerField(default=0)),
                ('preco', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('cor', models.CharField(default='', max_length=30)),
                ('marca', models.CharField(default='', max_length=30)),
            ],
        ),
    ]
