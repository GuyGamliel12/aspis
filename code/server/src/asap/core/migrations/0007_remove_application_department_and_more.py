# Generated by Django 4.2 on 2023-04-25 08:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ('core', '0006_remove_application_department_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='application',
            name='state_Application',
            field=models.TextField(
                choices=[('ACTIVE', 'State 0'), ('DELAYED', 'State 1'), ('REJECTED', 'State 2'), ('OLD', 'State 3')],
                default=None, max_length=80),
        ),
    ]
