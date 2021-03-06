# Generated by Django 3.0.6 on 2020-05-18 11:04

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
            name='Package',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=64, unique=True)),
                ('description', models.TextField(max_length=1024)),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=32)),
                ('last_name', models.CharField(max_length=32)),
                ('national_code', models.CharField(max_length=10, unique=True)),
                ('is_supervisor', models.BooleanField(default=False)),
                ('mobile', models.CharField(max_length=16)),
                ('phone', models.CharField(max_length=16)),
                ('created_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Stuff',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=64, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='PersonPackage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('status', models.SmallIntegerField(choices=[(1, 'Distributing'), (2, 'Delivered'), (3, 'Returned')], default=1)),
                ('distributor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
                ('package', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sky.Package')),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sky.Person')),
            ],
        ),
        migrations.AddField(
            model_name='person',
            name='packages',
            field=models.ManyToManyField(through='sky.PersonPackage', to='sky.Package'),
        ),
        migrations.AddField(
            model_name='package',
            name='stuffs',
            field=models.ManyToManyField(to='sky.Stuff'),
        ),
    ]
