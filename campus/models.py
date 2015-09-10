#coding=utf8
from django.db import models

# Create your models here.
from django.forms import ModelForm


class Student(models.Model):

    email = models.CharField(primary_key=True, max_length=45, verbose_name=u'邮箱')
    name = models.CharField(max_length=45, verbose_name=u'姓名')
    phone = models.CharField(max_length=45, verbose_name=u'号码')
    studentID = models.CharField(max_length=45, verbose_name=u'学生ID')
    message = models.CharField(max_length=45, verbose_name=u'内容')
    # status = models.CharField(max_length=45, verbose_name=u'状态')
    addTime = models.DateTimeField(auto_now_add=True, verbose_name=u'修改时间')

    def __unicode__(self):
        return u'%s %s' % (self.name, self.studentID)

    class Meta:
        ordering = ['studentID', 'name']
        verbose_name_plural = verbose_name = u'报名信息'


class StudentForm(ModelForm):
    class Meta:
        model = Student
        fields = ('name', 'email', 'phone', 'studentID', 'message')