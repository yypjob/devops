# Generated by Django 2.0.2 on 2018-05-09 04:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('db', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='menu',
            name='sub_menu',
        ),
        migrations.AddField(
            model_name='submenu',
            name='super_menu',
            field=models.ManyToManyField(to='db.Menu'),
        ),
    ]