# Generated manually

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("contacts", "0002_alter_contactrequest_subject"),
    ]

    operations = [
        migrations.AlterField(
            model_name="contactrequest",
            name="subject",
            field=models.CharField(
                default="other",
                max_length=100,
                verbose_name="Категорія продукту",
            ),
        ),
    ]
