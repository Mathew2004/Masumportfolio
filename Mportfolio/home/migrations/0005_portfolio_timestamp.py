# Generated by Django 4.2.4 on 2023-11-25 16:16

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_portfolio_alter_home_img'),
    ]

    operations = [
        migrations.AddField(
            model_name='portfolio',
            name='timestamp',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]