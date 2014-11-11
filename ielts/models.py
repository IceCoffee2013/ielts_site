#coding=utf8

from django.db import models

# Create your models here.
class Seat(models.Model):

    seatId = models.CharField(primary_key=True, max_length=45, verbose_name=u'考位代码')
    center = models.CharField(max_length=45, verbose_name=u'考点')
    date = models.DateField(verbose_name=u'日期')
    city = models.CharField(max_length=45, verbose_name=u'城市')
    province = models.CharField(max_length=45, verbose_name=u'省份')
    status = models.CharField(max_length=45, verbose_name=u'状态')
    addTime = models.DateTimeField(auto_now_add=True, verbose_name=u'修改时间')

    def __unicode__(self):
        return u'%s %d' % (self.date, self.center)

    class Meta:
        ordering = ['date', 'province', 'city', 'center']
        verbose_name_plural = verbose_name = u'考位信息'