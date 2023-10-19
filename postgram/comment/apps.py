from django.apps import AppConfig


class CommentConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "postgram.comment"
    label = "postgram_comment"
