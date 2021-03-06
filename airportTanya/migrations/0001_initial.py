# Generated by Django 3.0.6 on 2020-05-25 10:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Airline',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='Название авиакомпании')),
                ('dataAir', models.CharField(max_length=20, verbose_name='Дата основании авиакомпании')),
                ('typeAir', models.CharField(max_length=100, verbose_name='Тип воздушного судна')),
            ],
        ),
        migrations.CreateModel(
            name='Airport',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='Название аэропорта')),
                ('dateEst', models.CharField(max_length=20, verbose_name='Дата основания')),
                ('location', models.CharField(max_length=40, verbose_name='Местоположение')),
                ('workTime', models.CharField(max_length=100, verbose_name='Режим работы')),
                ('airBD', models.CharField(max_length=20, null=True, verbose_name='Авиакомпании')),
            ],
        ),
        migrations.CreateModel(
            name='Route',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fromRoute', models.CharField(max_length=20, verbose_name='Вылет в')),
                ('toRoute', models.CharField(max_length=20, verbose_name='Прилет в')),
                ('dataRoute', models.CharField(max_length=100, verbose_name='Дата и время вылета')),
                ('airlineID', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='airportTanya.Airline')),
            ],
        ),
        migrations.AddField(
            model_name='airline',
            name='airportID',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='airportTanya.Airport'),
        ),
    ]
