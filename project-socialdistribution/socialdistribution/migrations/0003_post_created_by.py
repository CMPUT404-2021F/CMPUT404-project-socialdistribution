# Generated by Django 3.2.8 on 2021-10-29 00:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('socialdistribution', '0002_post_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='created_by',
            field=models.CharField(default='Author', max_length=200),
        ),
    ]
