# Generated by Django 4.1 on 2022-08-29 06:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_remove_user_teacher'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='teacher',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='students', to=settings.AUTH_USER_MODEL),
        ),
    ]
