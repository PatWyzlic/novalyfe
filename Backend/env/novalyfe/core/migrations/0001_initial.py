# Generated by Django 4.0.6 on 2022-07-27 17:56

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
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateField(auto_now_add=True)),
                ('email', models.EmailField(max_length=254)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ToDo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('created_date', models.DateField(auto_now_add=True)),
                ('start_date', models.DateField()),
                ('due_date', models.DateField()),
                ('color', models.CharField(choices=[('0', 'Black'), ('1', 'White'), ('2', 'Blue'), ('3', 'Red'), ('4', 'Green'), ('5', 'Brown'), ('6', 'Grey'), ('7', 'Pink'), ('8', 'Purple'), ('9', 'Orange'), ('10', 'Yellow'), ('11', 'Darkolive'), ('12', 'Lightpink'), ('13', 'Lightblue')], default='Black', max_length=5)),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.profile')),
            ],
        ),
        migrations.CreateModel(
            name='RoutineItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('created_date', models.DateField(auto_now_add=True)),
                ('start_date', models.DateField()),
                ('due_date', models.DateField()),
                ('repetition_amount', models.IntegerField()),
                ('color', models.CharField(choices=[('0', 'Black'), ('1', 'White'), ('2', 'Blue'), ('3', 'Red'), ('4', 'Green'), ('5', 'Brown'), ('6', 'Grey'), ('7', 'Pink'), ('8', 'Purple'), ('9', 'Orange'), ('10', 'Yellow'), ('11', 'Darkolive'), ('12', 'Lightpink'), ('13', 'Lightblue')], default='Black', max_length=5)),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.profile')),
            ],
        ),
        migrations.CreateModel(
            name='Animal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('color', models.CharField(max_length=25)),
                ('breed', models.CharField(max_length=40)),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.profile')),
            ],
        ),
    ]
