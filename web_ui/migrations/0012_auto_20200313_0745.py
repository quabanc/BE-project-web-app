# Generated by Django 3.0.3 on 2020-03-13 07:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web_ui', '0011_auto_20200313_0740'),
    ]

    operations = [
        migrations.RenameField(
            model_name='quizcompleted',
            old_name='options_selected',
            new_name='option_selected',
        ),
    ]
