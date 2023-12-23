# Generated by Django 4.2.8 on 2023-12-23 12:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('email_address', models.EmailField(max_length=254)),
                ('message', models.TextField()),
                ('phone', models.CharField(max_length=14, verbose_name='Əlaqə nömrəsi')),
            ],
            options={
                'verbose_name': 'Əlaqə formu',
                'verbose_name_plural': 'Əlaqə formu',
            },
        ),
    ]