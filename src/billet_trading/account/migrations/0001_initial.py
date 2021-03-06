# Generated by Django 2.2.3 on 2019-07-22 02:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('email', models.EmailField(max_length=60, unique=True, verbose_name='email')),
                ('username', models.CharField(max_length=30, unique=True)),
                ('date_joined', models.DateTimeField(auto_now_add=True, verbose_name='date joined')),
                ('last_login', models.DateTimeField(auto_now=True, verbose_name='last login')),
                ('is_admin', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_superuse', models.BooleanField(default=False)),
                ('rank', models.CharField(choices=[('E-1', 'E-1'), ('E-2', 'E-2'), ('E-3', 'E-3'), ('E-4', 'E-4'), ('E-5', 'E-5'), ('E-6', 'E-6'), ('E-7', 'E-7'), ('E-8', 'E-8'), ('E-9', 'E-9')], max_length=3)),
                ('squadron', models.CharField(max_length=15)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
