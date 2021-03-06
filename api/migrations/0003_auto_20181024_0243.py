# Generated by Django 2.1.2 on 2018-10-24 02:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20181023_1138'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaction',
            name='amount',
            field=models.FloatField(default=None, null=True),
        ),
        migrations.AlterField(
            model_name='wallet',
            name='initial_balance',
            field=models.FloatField(default=0),
        ),
    ]
