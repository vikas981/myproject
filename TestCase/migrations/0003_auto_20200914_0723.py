# Generated by Django 3.1.1 on 2020-09-14 07:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TestCase', '0002_auto_20200914_0710'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testcasedetail',
            name='status',
            field=models.CharField(choices=[('Approved', 'Approved'), ('Disapproved', 'Disapproved')], max_length=20, null=True),
        ),
    ]
