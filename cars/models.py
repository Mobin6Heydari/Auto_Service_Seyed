from django.db import models





class CarsModel(models.Model):
    name = models.CharField(verbose_name="اسم ماشین", blank=True, null=True, max_length=30)
    brand = models.CharField(verbose_name="برند ماشین", blank=True, null=True, max_length=30)
    qaulity_ois = models.CharField(verbose_name="کیفیت روغن", blank=True, null=True, max_length=40)
    liter_oils = models.IntegerField(verbose_name="ظرفیت روغن", blank=True, null=True)
    sug_oils = models.CharField(verbose_name="روغن های بیشنهادی ما", blank=True, null=True, max_length=40)
    main_image = models.ImageField(verbose_name="عکس ماشین", blank=True, null=True, upload_to="cars1")
    second_img = models.ImageField(verbose_name="عکس دوم", blank=True, null=True, upload_to="cars2")
    third_img = models.ImageField(verbose_name="عکس سوم", blank=True, null=True, upload_to="cars3")



    def __str__(self):
        return self.name
    



    class Meta:
        verbose_name_plural = "ماشین ها "