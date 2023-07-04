from django.db import models

# Create your models here.


class ConatctModel(models.Model):
    addres = models.CharField(verbose_name="آدرس",
                               blank=True, null=True, max_length=60)
    phone = models.BigIntegerField(verbose_name="شماره تلفن مغازه", 
                                          blank=True, null=True, help_text="0912----")
    email = models.EmailField(verbose_name="ایمیل", 
                                          blank=True, null=True, help_text="mobin@gmail.com")
    instagram_id = models.CharField(verbose_name="آیدی اینستا گرام", 
                                          blank=True, null=True, help_text="id", max_length=30)
    instagram_link = models.URLField(verbose_name="لینک اینستا گرام", 
                                          blank=True, null=True, help_text="link")
    
    def __str__(self):
        return self.addres
    

    class Meta:
        verbose_name_plural = "تماس با ما"
    



class UserContactModel(models.Model):
    name = models.CharField(verbose_name="اسم کاربر", blank=True, null=True, max_length=40)
    content = models.CharField(verbose_name="موضوع", blank=True, null=True, max_length=40)
    email = models.EmailField(verbose_name="ایمیل", blank=True, null=True)
    phone = models.CharField(verbose_name="شماره تلفن کاربر", blank=True, null=True, max_length=12)
    comment = models.TextField(verbose_name="سوال یا نظرر کابر", blank=True, null=True, max_length=500)


    def __str__(self):
        return self.name
    

    class Meta:
        verbose_name_plural = "تماس کاربر"