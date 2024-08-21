



import django.core.validators
import django.db.models.deletion
from django.conf import settings
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Specialization",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name="Mechanic",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "years_of_experience",
                    models.PositiveIntegerField(
                        blank=True,
                        null=True,
                        validators=[django.core.validators.MinValueValidator(0)],
                    ),
                ),
                (
                    "preferred_job_types",
                    models.CharField(
                        choices=[
                            ("Full-time", "Full-time"),
                            ("Part-time", "Part-time"),
                            ("Freelance", "Freelance"),
                        ],
                        max_length=50,
                    ),
                ),
                ("address", models.TextField(blank=True, null=True)),
                (
                    "gender",
                    models.CharField(
                        choices=[("M", "Male"), ("F", "Female")], max_length=1
                    ),
                ),
                (
                    "contact_number",
                    models.CharField(
                        max_length=15,
                        validators=[
                            django.core.validators.RegexValidator(
                                message="Contact number should be 9 digits.",
                                regex="^\\d{9}$",
                            )
                        ],
                    ),
                ),
                (
                    "profile_image",
                    models.ImageField(
                        blank=True, null=True, upload_to="profile_images/"
                    ),
                ),
                (
                    "user",
                    models.OneToOneField(
                        default=1,
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "specializations",
                    models.ManyToManyField(
                        related_name="mechanics", to="Mechanic.specialization"
                    ),
                ),
            ],
            options={
                "verbose_name_plural": "Mechanic",
            },
        ),
    ]
