# Generated by Django 3.2.9 on 2022-04-28 04:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sketchyactivity', '0009_auto_20211206_1831'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('description', models.CharField(max_length=150)),
                ('type', models.TextField()),
                ('price', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Purchase',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(auto_created=True)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sketchyactivity.product')),
                ('user_profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sketchyactivity.userprofile')),
            ],
        ),
        migrations.AddField(
            model_name='userprofile',
            name='cart',
            field=models.ManyToManyField(to='sketchyactivity.Product'),
        ),
    ]
