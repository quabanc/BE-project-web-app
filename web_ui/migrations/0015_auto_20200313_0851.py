# Generated by Django 3.0.3 on 2020-03-13 08:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web_ui', '0014_auto_20200313_0843'),
    ]

    operations = [
        migrations.RenameField(
            model_name='questionscompleted',
            old_name='options_selected',
            new_name='option_selected',
        ),
    ]
