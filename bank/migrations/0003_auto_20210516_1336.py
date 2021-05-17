# Generated by Django 3.2 on 2021-05-16 08:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bank', '0002_auto_20210516_1210'),
    ]

    operations = [
        migrations.AddField(
            model_name='bank',
            name='bank_name',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='bank',
            name='bank_id',
            field=models.BigIntegerField(default=''),
        ),
    ]
