# Generated by Django 4.2.6 on 2023-10-18 09:25

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("postgram_post", "0001_initial"),
        ("postgram_user", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="posts_liked",
            field=models.ManyToManyField(
                related_name="liked_by", to="postgram_post.post"
            ),
        ),
    ]
