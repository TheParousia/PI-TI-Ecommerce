# Generated by Django 5.1.1 on 2024-09-16 23:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='batcaverna',
            name='imagem',
            field=models.ImageField(blank=True, null=True, upload_to='imagens/'),
        ),
    ]