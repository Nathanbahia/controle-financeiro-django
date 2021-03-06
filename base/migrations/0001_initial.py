# Generated by Django 3.1 on 2020-08-27 14:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BaseUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, verbose_name='E-mail')),
            ],
        ),
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(choices=[('RECEITAS', 'RECEITAS'), ('DESPESAS', 'DESPESAS')], max_length=8, verbose_name='Tipo')),
                ('categoria', models.CharField(max_length=50, verbose_name='Categoria')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.baseuser')),
            ],
            options={
                'verbose_name': 'Categoria',
                'verbose_name_plural': 'Categorias',
            },
        ),
        migrations.CreateModel(
            name='Movimento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.DateField(verbose_name='Data')),
                ('descricao', models.CharField(max_length=100, verbose_name='Descrição')),
                ('valor', models.FloatField(verbose_name='Valor')),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.categoria')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.baseuser')),
            ],
            options={
                'verbose_name': 'Movimento',
                'verbose_name_plural': 'Movimentos',
            },
        ),
    ]
