# Generated by Django 4.2.4 on 2023-11-28 07:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_contact'),
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('shortDes', models.CharField(max_length=350)),
                ('experience', models.TextField()),
                ('edu', models.TextField()),
                ('skill', models.TextField()),
                ('achive', models.TextField()),
            ],
        ),
    ]
