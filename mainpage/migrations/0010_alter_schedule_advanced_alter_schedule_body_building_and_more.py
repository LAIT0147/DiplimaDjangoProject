# Generated by Django 4.0.5 on 2022-06-04 11:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainpage', '0009_alter_trainer_facebook_alter_trainer_linkedin_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='schedule',
            name='advanced',
            field=models.CharField(default='-', max_length=15, unique=True),
        ),
        migrations.AlterField(
            model_name='schedule',
            name='body_building',
            field=models.CharField(default='-', max_length=15, unique=True),
        ),
        migrations.AlterField(
            model_name='schedule',
            name='fitness',
            field=models.CharField(default='-', max_length=15, unique=True),
        ),
        migrations.AlterField(
            model_name='schedule',
            name='muscle',
            field=models.CharField(default='-', max_length=15, unique=True),
        ),
        migrations.AlterField(
            model_name='schedule',
            name='yoga',
            field=models.CharField(default='-', max_length=15, unique=True),
        ),
    ]
