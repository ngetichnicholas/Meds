# Generated by Django 3.2.5 on 2021-07-29 09:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clinic_app', '0014_auto_20210728_1841'),
    ]

    operations = [
        migrations.AddField(
            model_name='patientappointment',
            name='approve',
            field=models.BooleanField(default=False),
        ),
    ]
