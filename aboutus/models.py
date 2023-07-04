from django.db import models

# Create your models here.



class AboutusModel(models.Model):
    name = models.CharField(verbose_name="نام", blank=True, null=True, max_length=20)
    experience = models.IntegerField(verbose_name="تجربه ی کاری", blank=True, null=True)
    description = models.TextField(verbose_name="توضیحات", blank=True, null=True, max_length=10000)
    image = models.ImageField(verbose_name="عکس", blank=True, null=True, upload_to="about_photo")


    def __str__(self):
        return self.name
    

    class Meta:
        verbose_name_plural = "درباره ما"