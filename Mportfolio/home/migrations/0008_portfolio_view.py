# Generated by Django 4.2.4 on 2023-11-28 14:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_about'),
    ]

    operations = [
        migrations.AddField(
            model_name='portfolio',
            name='view',
            field=models.CharField(default='jds', max_length=350),
            preserve_default=False,
        ),
    ]