# Generated by Django 4.2.8 on 2023-12-23 12:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('general', '0002_deyisebilencontact'),
    ]

    operations = [
        migrations.AlterField(
            model_name='deyisebilencontact',
            name='desc',
            field=models.CharField(max_length=255, verbose_name='Bizimlə əlaqə haqqında qısa məlumat'),
        ),
        migrations.AlterField(
            model_name='deyisebilencontact',
            name='title',
            field=models.CharField(max_length=255, verbose_name='Başlıq ilk'),
        ),
        migrations.AlterField(
            model_name='deyisebilencontact',
            name='title_2',
            field=models.CharField(max_length=255, verbose_name='Başlıq sağ tərəf'),
        ),
        migrations.AlterField(
            model_name='deyisebilencontact',
            name='unvan',
            field=models.CharField(max_length=255, verbose_name='Şirkət Ünvanı'),
        ),
    ]
