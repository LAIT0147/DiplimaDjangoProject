# Generated by Django 4.0.5 on 2022-06-04 11:30

from django.db import migrations, models
import mainpage.models


class Migration(migrations.Migration):

    dependencies = [
        ('mainpage', '0008_trainer_facebook_trainer_linkedin_trainer_photo_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trainer',
            name='facebook',
            field=models.CharField(default='-', max_length=20),
        ),
        migrations.AlterField(
            model_name='trainer',
            name='linkedin',
            field=models.CharField(default='-', max_length=200),
        ),
        migrations.AlterField(
            model_name='trainer',
            name='photo',
            field=models.ImageField(default='null', upload_to=mainpage.models.Trainer.get_file_name_trainer),
        ),
        migrations.AlterField(
            model_name='trainer',
            name='twitter',
            field=models.CharField(default='-', max_length=200),
        ),
    ]
