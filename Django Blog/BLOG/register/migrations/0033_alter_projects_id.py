# Generated by Django 5.0.7 on 2024-09-18 10:59

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0032_remove_projects_user_alter_projects_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projects',
            name='id',
            field=models.UUIDField(default=uuid.uuid1, primary_key=True, serialize=False),
        ),
    ]
