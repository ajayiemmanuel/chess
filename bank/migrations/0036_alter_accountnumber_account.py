# Generated by Django 4.2.4 on 2023-11-02 06:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bank', '0035_accountnumber'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accountnumber',
            name='account',
            field=models.CharField(default='Generating Account Number...', max_length=200),
        ),
    ]
