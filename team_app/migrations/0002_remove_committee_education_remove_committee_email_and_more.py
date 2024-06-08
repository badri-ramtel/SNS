# Generated by Django 4.2.13 on 2024-06-08 17:25

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('team_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='committee',
            name='education',
        ),
        migrations.RemoveField(
            model_name='committee',
            name='email',
        ),
        migrations.RemoveField(
            model_name='committee',
            name='profession',
        ),
        migrations.AddField(
            model_name='committee',
            name='bio',
            field=ckeditor.fields.RichTextField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='submenu',
            name='year',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='team_app.year_book'),
        ),
    ]