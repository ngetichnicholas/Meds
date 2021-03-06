# Generated by Django 3.2.5 on 2021-07-27 14:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('clinic_app', '0009_patientappointment'),
    ]

    operations = [
        migrations.CreateModel(
            name='PatientHealthHistory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('health_record', models.TextField()),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clinic_app.patient')),
            ],
        ),
    ]
