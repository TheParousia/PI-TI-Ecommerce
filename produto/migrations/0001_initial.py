# Essa MIgration será gerada novamente de maneira automática com o comando makemigrations
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
                ('username', models.CharField(max_length=150, unique=True)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('telefone', models.CharField(max_length=15)),
                ('cpf_cnpj', models.CharField(max_length=18)),
                ('cep', models.CharField(max_length=10)),
                ('rua', models.CharField(max_length=255)),
                ('numero', models.CharField(max_length=10)),
                ('bairro', models.CharField(max_length=255)),
                ('senha', models.CharField(max_length=128)),
            ],
        ),
    ]
