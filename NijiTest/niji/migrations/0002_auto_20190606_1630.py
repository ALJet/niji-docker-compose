# Generated by Django 2.2.1 on 2019-06-06 08:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('niji', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='topic',
            options={'ordering': ['order', '-pub_date']},
        ),
        migrations.AlterField(
            model_name='post',
            name='content_raw',
            field=models.TextField(verbose_name='raw content'),
        ),
    ]
