# Generated by Django 3.0 on 2019-12-23 09:17

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import multiselectfield.db.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='Job',
            fields=[
                ('Tutor', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('Profile_Pic', models.ImageField(default='/images/propic avater.jpg', upload_to='profile_pic/')),
                ('Gender', models.CharField(default='', max_length=10)),
                ('Phone', models.CharField(default='', max_length=15)),
                ('DOB', models.DateField(default=datetime.date(1111, 11, 11))),
                ('Address', models.TextField(default='', max_length=150)),
                ('Religion', models.CharField(default='', max_length=10)),
                ('Class', multiselectfield.db.fields.MultiSelectField(choices=[('PR', 'Primary (1-5)'), ('JU', 'Junior (6-8)'), ('SSC', 'Scondary (9-10)'), ('HSC', 'Higher Secondary (11-12)')], max_length=5)),
                ('Subject', multiselectfield.db.fields.MultiSelectField(choices=[('M', 'Math'), ('E', 'English'), ('P', 'Physics'), ('C', 'Chemistry'), ('B', 'Biology'), ('BN', 'Bangla'), ('I', 'ICT'), ('CM', 'Computer')], max_length=5)),
                ('Medium', multiselectfield.db.fields.MultiSelectField(choices=[('BM', 'Bangla Medium'), ('EM', 'English Medium'), ('EV', 'English Version(National Curriculam)')], default='', max_length=5)),
                ('Location', models.TextField(max_length=100)),
                ('Days', models.IntegerField()),
                ('Tution_Type', models.CharField(choices=[('PR', 'Private'), ('BC', 'Batch'), ('PB', 'Both Private and Batch')], default='', max_length=5)),
                ('Salary', models.TextField()),
                ('Institution', models.CharField(default='', max_length=100)),
                ('Degree', models.CharField(default='', max_length=100)),
                ('MySubject', models.CharField(default='', max_length=100)),
                ('Registration', models.CharField(default='', max_length=30)),
                ('Vote', models.IntegerField(default=0)),
            ],
        ),
    ]
