# Generated by Django 4.2.8 on 2023-12-23 12:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('general', '0004_deyisebilenhaqqimizda'),
    ]

    operations = [
        migrations.AlterField(
            model_name='deyisebilenhaqqimizda',
            name='desc',
            field=models.TextField(max_length=255, verbose_name='Haqqımızda məlumat'),
        ),
    ]
