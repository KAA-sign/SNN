# Generated by Django 3.2 on 2021-06-02 12:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0002_alter_profile_background'),
        ('posts', '0004_alter_post_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='author',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='profiles.profile'),
        ),
    ]
