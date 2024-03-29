# Generated by Django 2.2 on 2019-12-02 16:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='social',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_link', models.TextField()),
                ('post_link', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='trends',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=100)),
                ('header', models.TextField()),
                ('keywords', models.CharField(max_length=200)),
                ('image_link', models.TextField()),
                ('paragraph', models.TextField(blank=True, default=None, null=True)),
                ('video_link', models.TextField(blank=True, default=None, null=True)),
            ],
        ),
    ]
