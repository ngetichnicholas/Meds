# Generated by Django 3.2.5 on 2021-07-29 10:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clinic_app', '0016_alter_patientappointment_approve'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patientappointment',
            name='approve',
            field=models.CharField(choices=[('Approved', 'Approved'), ('Not Approved', 'Not Approved'), ('Pending', 'Pending')], default='Pending', max_length=15),
        ),
    ]