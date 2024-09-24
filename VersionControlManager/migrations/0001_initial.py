# Generated by Django 5.1.1 on 2024-09-24 00:34

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='VersionControlType',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('required_fields', models.JSONField(default=dict)),
            ],
        ),
        migrations.CreateModel(
            name='VersionControl',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('connection_name', models.CharField(max_length=100, unique=True)),
                ('data', models.JSONField()),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='version_controls', to='VersionControlManager.versioncontroltype')),
            ],
        ),
    ]