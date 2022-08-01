# Generated by Django 4.0.6 on 2022-08-01 19:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('created_date', models.DateField(auto_now_add=True)),
                ('name', models.CharField(max_length=100)),
                ('user_type_choices', models.CharField(choices=[('0', 'Admin'), ('1', 'Normal')], default='Normal', max_length=20)),
                ('profile_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ToDo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(null=True)),
                ('created_date', models.DateField(auto_now_add=True)),
                ('start_date', models.DateField()),
                ('due_date', models.DateField(null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='RoutineItem',
            fields=[
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(null=True)),
                ('created_date', models.DateField(auto_now_add=True)),
                ('start_date', models.DateField(null=True)),
                ('due_date', models.DateField()),
                ('repetition_amount', models.IntegerField(null=True)),
                ('color', models.CharField(choices=[('0', 'Black'), ('1', 'White'), ('2', 'Blue'), ('3', 'Red'), ('4', 'Green'), ('5', 'Brown'), ('6', 'Grey'), ('7', 'Pink'), ('8', 'Purple'), ('9', 'Orange'), ('10', 'Yellow'), ('11', 'Darkolive'), ('12', 'Lightpink'), ('13', 'Lightblue')], default='Black', max_length=5)),
                ('routine_item_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('profile', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='core.profile')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Animal',
            fields=[
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('color', models.CharField(max_length=25)),
                ('breed', models.CharField(max_length=40)),
                ('animal_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.profile')),
            ],
        ),
    ]
