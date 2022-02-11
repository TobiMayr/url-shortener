# Generated by Django 4.0.2 on 2022-02-11 21:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Url',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('original_url', models.TextField()),
                ('short_url', models.TextField()),
            ],
            options={
                'db_table': 'url',
            },
        ),
        migrations.AddIndex(
            model_name='url',
            index=models.Index(fields=['short_url'], name='url_short_u_0b2618_idx'),
        ),
    ]
