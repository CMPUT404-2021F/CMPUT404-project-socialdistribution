# Generated by Django 3.2.8 on 2021-11-24 23:44

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
                ('author', models.CharField(default='Author', max_length=200)),
                ('title', models.CharField(default='Title', max_length=200)),
                ('text', models.TextField()),
            ],
        ),
    ]
