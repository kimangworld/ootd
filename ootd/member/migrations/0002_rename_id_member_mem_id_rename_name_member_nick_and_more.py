# Generated by Django 4.0.1 on 2022-01-23 08:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('member', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='member',
            old_name='id',
            new_name='mem_id',
        ),
        migrations.RenameField(
            model_name='member',
            old_name='name',
            new_name='nick',
        ),
        migrations.RenameField(
            model_name='member',
            old_name='pass1',
            new_name='pw',
        ),
        migrations.AlterField(
            model_name='member',
            name='birth',
            field=models.DateField(),
        ),
    ]