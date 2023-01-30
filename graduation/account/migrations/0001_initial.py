# Generated by Django 4.1.5 on 2023-01-10 21:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Kindergarden',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('address', models.CharField(max_length=255)),
                ('rayon', models.CharField(max_length=30)),
                ('phone_number', models.CharField(max_length=20)),
                ('num_free_places', models.IntegerField(default=0, null=True)),
                ('num_register_child', models.IntegerField(default=0, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Child',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('surname', models.CharField(max_length=20)),
                ('id_number', models.CharField(max_length=20)),
                ('ochered', models.IntegerField(default=None, null=True)),
                ('det_sads', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.kindergarden', verbose_name='Детские сады')),
                ('roditeli', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Родители')),
            ],
            options={
                'verbose_name': 'Ребенок',
            },
        ),
    ]
