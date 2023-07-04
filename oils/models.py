from django.db import models

# Create your models here.



class ProductModel(models.Model):
    type = models.CharField(verbose_name="دسته بندی محصول", blank=True, null=True, max_length=40)
    name = models.CharField(verbose_name="اسم محصول", blank=True, null=True, max_length=40)
    brand = models.CharField(verbose_name="برند محصول", blank=True, null=True, max_length=40)
    description = models.TextField(verbose_name="اطلاعات", blank=True, null=True, max_length=500)
    price = models.BigIntegerField(verbose_name="قیمت", blank=True, null=True)
    sug_cars = models.CharField(verbose_name="ماشین های بیشنهادی ما", blank=True, null=True, max_length=40)
    main_image = models.ImageField(verbose_name="عکس اصلی", blank=True, null=True, upload_to= "product1")
    second_img = models.ImageField(verbose_name="عکس دوم", blank=True, null=True, upload_to= "product2")
    third_img = models.ImageField(verbose_name="عکس سوم", blank=True, null=True, upload_to= "product3")


    def __str__(self):
        return self.name
    

    class Meta:
        verbose_name_plural = "محصولات"