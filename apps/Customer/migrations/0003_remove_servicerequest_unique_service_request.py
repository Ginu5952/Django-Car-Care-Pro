# Generated by Django 5.0.7 on 2024-09-01 13:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("Customer", "0002_servicerequest_due_date"),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name="servicerequest",
            name="unique_service_request",
        ),
    ]
