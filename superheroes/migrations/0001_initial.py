# Generated by Django 3.0.6 on 2020-05-28 20:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Publisher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(blank=True, default='', max_length=100)),
                ('founder', models.CharField(blank=True, default='', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='SuperHeroe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(blank=True, default='', max_length=100)),
                ('gender', models.CharField(blank=True, default='', max_length=100)),
                ('real_name', models.CharField(blank=True, default='', max_length=100)),
                ('publisher', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='superheroes.Publisher')),
            ],
        ),
    ]