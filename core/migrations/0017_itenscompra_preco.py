# Generated by Django 5.1.4 on 2024-12-15 20:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0016_editora_email"),
    ]

    operations = [
        migrations.AddField(
            model_name="itenscompra",
            name="preco",
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
    ]