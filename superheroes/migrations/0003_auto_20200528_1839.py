# Generated by Django 3.0.6 on 2020-05-28 21:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('superheroes', '0002_auto_20200528_1828'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='SuperHeroe',
            new_name='Heroe',
        ),
        migrations.AlterModelOptions(
            name='heroe',
            options={'ordering': ('name',)},
        ),
        migrations.AlterModelOptions(
            name='publisher',
            options={'ordering': ('name',)},
        ),
        migrations.RenameField(
            model_name='heroe',
            old_name='nombre',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='publisher',
            old_name='nombre',
            new_name='name',
        ),
    ]
