# Generated by Django 4.2.5 on 2023-10-05 19:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0003_alter_habits_frequency'),
    ]

    operations = [
        migrations.AddField(
            model_name='habits',
            name='time_last_send',
            field=models.DateTimeField(blank=True, null=True, verbose_name='последняя отпрвка уведомления'),
        ),
    ]
