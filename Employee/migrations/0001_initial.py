# Generated by Django 3.1.3 on 2020-11-26 08:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employees',
            fields=[
                ('EmployeeId', models.AutoField(primary_key=True, serialize=False)),
                ('EmployeeName', models.CharField(max_length=100)),
                ('EmployeeAddress', models.CharField(max_length=255)),
                ('EmployeeEmail', models.EmailField(max_length=254)),
                ('EmployeePhoneNumber', models.IntegerField()),
                ('EmployeeImage', models.ImageField(upload_to='img/%y')),
            ],
        ),
    ]
