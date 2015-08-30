#coding=utf8
from django.db import models

# Create your models here.
class Account(models.Model):

    mail = models.CharField(primary_key=True, max_length=45, verbose_name=u'邮箱')
    name = models.CharField(max_length=45, verbose_name=u'姓名')
    phone = models.CharField(max_length=45,verbose_name=u'手机')
    cardId = models.CharField(max_length=45, verbose_name=u'身份证号')
    userName = models.CharField(max_length=45, verbose_name=u'用户名')
    key = models.CharField(max_length=45, verbose_name=u'密码')

    def __unicode__(self):
        return u'%s %s' % (self.date, self.center)

    class Meta:
        ordering = ['mail', 'name', 'phone', 'cardId']
        verbose_name_plural = verbose_name = u'12306信息'