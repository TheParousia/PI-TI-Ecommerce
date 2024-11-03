# Essa MIgration será gerada novamente de maneira automática com o comando makemigrations
import django.db.models.deletion
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
                ('descricao', models.CharField(max_length=100)),
                ('capacidade1', models.CharField(max_length=10)),
                ('capacidade2', models.CharField(max_length=10)),
                ('capacidade3', models.CharField(max_length=10)),
                ('qtd_estoque', models.IntegerField(default=0)),
                ('preco', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('imagem1', models.ImageField(default='img/default.jpg', upload_to='produto')),
                ('imagem2', models.ImageField(default='img/default.jpg', upload_to='produto')),
                ('imagem3', models.ImageField(default='img/default.jpg', upload_to='produto')),
                ('imagem4', models.ImageField(default='img/default.jpg', upload_to='produto')),
                ('acessos', models.IntegerField(default=0)),
                ('cor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='produto.cor')),
                ('marca', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='produto.marca')),
                ('modelo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='produto.modelo')),
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
