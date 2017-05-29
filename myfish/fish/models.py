# -*- coding: UTF-8 -*-
from django.db import models


# Create your models here.
class FishPhoto(models.Model):
    createdAt = models.DateTimeField(auto_now_add=True, verbose_name=u"创建于")
    photo = models.ImageField(verbose_name=u"图片")

    def __unicode__(self):
        return "%s" % self.createdAt

    class Meta:
        verbose_name = u"鱼缸照片"
        verbose_name_plural = u"鱼缸照片"
