# Generated by Django 4.0.5 on 2022-06-04 10:12

from django.db import migrations, models
import mainpage.models


class Migration(migrations.Migration):

    dependencies = [
        ('mainpage', '0003_days'),
    ]

    operations = [
        migrations.AddField(
            model_name='classes',
            name='photo',
            field=models.ImageField(default=0, upload_to=mainpage.models.Classes.get_file_name),
            preserve_default=False,
        ),
    ]
