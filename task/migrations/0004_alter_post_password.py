# Generated by Django 4.1 on 2022-09-21 15:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0003_alter_post_password'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='password',
            field=models.IntegerField(),
        ),
    ]
