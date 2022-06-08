# Generated by Django 4.0.5 on 2022-06-04 11:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainpage', '0006_alter_trainer_desc_alter_trainer_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='trainer',
            name='facebook',
        ),
        migrations.RemoveField(
            model_name='trainer',
            name='linkedin',
        ),
        migrations.RemoveField(
            model_name='trainer',
            name='photo',
        ),
        migrations.RemoveField(
            model_name='trainer',
            name='twitter',
        ),
        migrations.AddField(
            model_name='trainer',
            name='expert',
            field=models.BooleanField(default=False),
        ),
    ]
