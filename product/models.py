from django.db import models

from core.models import LogicalBaseModel, StatusMixin, TimeStampBaseModel


class Product(LogicalBaseModel, StatusMixin, TimeStampBaseModel):
    title = models.CharField(max_length=200)


class OrderedProduct(Product):
    class Meta:
        ordering = ['created_at']
        proxy = True


# OrderedProduct.objects.all() == Product.objects.all().order_by('created_at')


class Image(models.Model):
    src = models.ImageField(upload_to='images/')
    alt = models.CharField(max_length=255)


# class BannerImage(models.Model):
#     image = models.OneToOneField(Image, on_delete=models.CASCADE)
#     available = models.BooleanField(default=True)
#     priority = models.IntegerField(default=0)
#     link = models.CharField(max_length=255, blank=True, null=True)
#     expired = models.DateTimeField(blank=True, null=True)


# img = Image.objects.create(src='...', alt="...")
# BannerImage.objects.create(image=img, link="https://google.com")


class BannerImage(Image):
    available = models.BooleanField(default=True)
    priority = models.IntegerField(default=0)
    link = models.CharField(max_length=255, blank=True, null=True)
    expired = models.DateTimeField(blank=True, null=True)


# BannerImage.objects.create(src="...", alt="...", link="https://google.com")
