from django.db import models

# Create your models here.
class Contact(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email_address = models.EmailField()
    message = models.TextField()
    phone = models.CharField(max_length=14, verbose_name='Əlaqə nömrəsi')

    class Meta:
        verbose_name = 'Əlaqə formu'
        verbose_name_plural = 'Əlaqə formu'

    def __str__(self):
        return self.first_name
    
class DeyisebilenContact(models.Model):
    title = models.CharField(max_length=255, verbose_name='Başlıq ilk')
    title_2 = models.CharField(max_length=255, verbose_name='Başlıq sağ tərəf')
    desc = models.CharField(max_length=255, verbose_name='Bizimlə əlaqə haqqında qısa məlumat')
    phone = models.CharField(max_length=14, verbose_name='Əlaqə nömrəsi')
    email_address = models.EmailField(verbose_name='Şirkət E-poçtu')
    unvan = models.CharField(max_length=255, verbose_name='Şirkət Ünvanı')


    class Meta:
        verbose_name = 'Əlaqə səhifəsi dəyiş'
        verbose_name_plural = 'Əlaqə səhifəsi dəyiş'

    def __str__(self):
        return self.title
    

class DeyisebilenHaqqimizda(models.Model):
    title = models.CharField(max_length=255, verbose_name='Başlıq ilk')
    title_2 = models.CharField(max_length=255, verbose_name='Başlıq ikinci')
    desc = models.TextField(verbose_name='Haqqımızda məlumat')
    image = models.ImageField(upload_to='haqqimizda/', verbose_name='Haqqımızda Şəkli')



    class Meta:
        verbose_name = 'Haqqımızda səhifəsi dəyiş'
        verbose_name_plural = 'Haqqımızda səhifəsi dəyiş'

    def __str__(self):
        return self.title