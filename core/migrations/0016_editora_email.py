# Generated by Django 5.1.4 on 2024-12-15 20:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0015_itenscompra"),
    ]

    operations = [
        migrations.AddField(
            model_name="editora",
            name="email",
            field=models.CharField(default="editora@teste.com", max_length=100),
            preserve_default=False,
        ),
    ]
