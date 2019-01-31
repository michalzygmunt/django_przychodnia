# Generated by Django 2.1.5 on 2019-01-24 12:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Lekarz',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nazwa', models.CharField(max_length=30, verbose_name='Lekarz')),
                ('opis', models.TextField(blank=True, help_text='Opis Lekarza')),
                ('cena', models.DecimalField(decimal_places=0, max_digits=5)),
                ('data', models.DateField(auto_now_add=True, verbose_name='dodano')),
            ],
        ),
        migrations.CreateModel(
            name='Specjalizacja',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nazwa', models.CharField(max_length=30, verbose_name='specjalizacja')),
                ('jarski', models.BooleanField(default=False, help_text='Zaznacz, jeżeli składnik jest odpowiedni dla dzieci', verbose_name='Czy dla osob ponizej 18 lat?')),
                ('lekarz', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='specjalizacje', to='przychodnia.Lekarz')),
            ],
        ),
    ]
