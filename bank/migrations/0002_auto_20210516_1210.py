# Generated by Django 3.2 on 2021-05-16 06:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bank', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bank',
            name='description',
        ),
        migrations.RemoveField(
            model_name='bank',
            name='published',
        ),
        migrations.RemoveField(
            model_name='bank',
            name='title',
        ),
        migrations.AddField(
            model_name='bank',
            name='address',
            field=models.CharField(default='', max_length=195),
        ),
        migrations.AddField(
            model_name='bank',
            name='bank_id',
            field=models.BigIntegerField(default=''),
        ),
        migrations.AddField(
            model_name='bank',
            name='branch',
            field=models.CharField(default='', max_length=74),
        ),
        migrations.AddField(
            model_name='bank',
            name='city',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='bank',
            name='district',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='bank',
            name='ifsc',
            field=models.CharField(default='', max_length=11),
        ),
        migrations.AddField(
            model_name='bank',
            name='state',
            field=models.CharField(default='', max_length=26),
        ),
    ]