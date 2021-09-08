from django.db import models

# Create your models here.
class Image(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    ImgName = models.CharField(max_length=100)
    ImgURL = models.URLField()
    ImgDetails = models.TextField(max_length=500)

    class Meta:
        ordering = ('-id',)