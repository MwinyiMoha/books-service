# Generated by Django 3.2 on 2021-04-10 12:31

from decimal import Decimal
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("books", "0002_remove_bookrent_user")]

    operations = [
        migrations.AddField(
            model_name="book",
            name="category",
            field=models.CharField(
                choices=[
                    ("fiction", "Fiction"),
                    ("fiction", "Fiction"),
                    ("fiction", "Fiction"),
                ],
                default="regular",
                max_length=7,
            ),
        ),
        migrations.AddField(
            model_name="book",
            name="price",
            field=models.DecimalField(
                decimal_places=2, default=Decimal("1.5"), max_digits=10
            ),
        ),
    ]
