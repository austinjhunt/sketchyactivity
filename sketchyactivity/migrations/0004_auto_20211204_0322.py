# Generated by Django 3.0 on 2021-12-04 03:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sketchyactivity', '0003_auto_20210906_1434'),
    ]

    operations = [
        migrations.AddField(
            model_name='price',
            name='num_subjects',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='price',
            name='size',
            field=models.CharField(default='8.5x12in', max_length=100),
        ),
        migrations.AddField(
            model_name='price',
            name='style',
            field=models.CharField(choices=[('TR', 'Traditional'), ('DI', 'Digital')], default='TR', max_length=2),
        ),
    ]
