# Generated by Django 3.0.6 on 2020-05-13 05:07

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=True)),
                ('description', models.CharField(max_length=300, null=True)),
                ('author', models.CharField(max_length=50, null=True)),
                ('create_date', models.DateField(default=datetime.datetime.now, null=True)),
                ('last_edit_date', models.DateField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('activity_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='activities.Activity')),
                ('event_details', models.CharField(max_length=100, null=True)),
            ],
            bases=('activities.activity',),
        ),
        migrations.CreateModel(
            name='Routine',
            fields=[
                ('activity_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='activities.Activity')),
                ('routine_details', models.CharField(max_length=100, null=True)),
            ],
            bases=('activities.activity',),
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('activity_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='activities.Activity')),
                ('task_details', models.CharField(max_length=100, null=True)),
            ],
            bases=('activities.activity',),
        ),
    ]