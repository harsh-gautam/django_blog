# Generated by Django 3.1.3 on 2021-01-06 16:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('post_id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=255, unique=True)),
                ('author', models.CharField(max_length=80)),
                ('content', models.TextField()),
                ('slug', models.CharField(max_length=255)),
                ('timestamp', models.DateTimeField()),
            ],
        ),
    ]
