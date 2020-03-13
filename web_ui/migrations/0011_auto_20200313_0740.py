# Generated by Django 3.0.3 on 2020-03-13 07:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('web_ui', '0010_auto_20200312_1741'),
    ]

    operations = [
        migrations.CreateModel(
            name='QuizCompleted',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('options_selected', models.TextField()),
                ('correct', models.BooleanField()),
                ('quiz', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='web_ui.Quiz')),
            ],
        ),
        migrations.AddField(
            model_name='multiuser',
            name='quiz_completed',
            field=models.ManyToManyField(to='web_ui.QuizCompleted'),
        ),
    ]