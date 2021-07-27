# Generated by Django 3.2.5 on 2021-07-27 13:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('clinic_app', '0007_medicine'),
    ]

    operations = [
        migrations.CreateModel(
            name='Prescription',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('note', models.TextField()),
                ('drug', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clinic_app.medicine')),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clinic_app.patient')),
                ('prescriber', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clinic_app.clinicalstaff')),
            ],
        ),
    ]