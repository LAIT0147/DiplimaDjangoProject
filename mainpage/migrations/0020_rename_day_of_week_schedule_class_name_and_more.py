# Generated by Django 4.0.5 on 2022-06-04 13:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainpage', '0019_rename_class_name_schedule_day_of_week'),
    ]

    operations = [
        migrations.RenameField(
            model_name='schedule',
            old_name='day_of_week',
            new_name='class_name',
        ),
        migrations.RenameField(
            model_name='schedule',
            old_name='advanced',
            new_name='friday',
        ),
        migrations.RenameField(
            model_name='schedule',
            old_name='body_building',
            new_name='monday',
        ),
        migrations.RenameField(
            model_name='schedule',
            old_name='fitness',
            new_name='thursday',
        ),
        migrations.RenameField(
            model_name='schedule',
            old_name='muscle',
            new_name='tuesday',
        ),
        migrations.RenameField(
            model_name='schedule',
            old_name='yoga',
            new_name='wednesday',
        ),
        migrations.AddField(
            model_name='schedule',
            name='trainer',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to='mainpage.trainer'),
            preserve_default=False,
        ),
    ]
