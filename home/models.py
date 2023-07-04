from django.db import models

# Create your models here.

class Logo(models.Model):
    logo = models.ImageField(verbose_name="لوگو", blank=True, null=True, upload_to="logo")

    class Meta:
        verbose_name_plural = "لوگو"