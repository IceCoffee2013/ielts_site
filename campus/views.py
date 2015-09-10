#coding=utf8
import logging
from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.
from django.template import loader, Context
from campus.models import Student, StudentForm
import sys
reload(sys)
sys.setdefaultencoding( "utf-8" )

def home(request):
    seats = []
    t = loader.get_template("campus_index.html")
    c = Context({'seats': seats})
    return HttpResponse(t.render(c))

def join_post(request):

    if request.method == 'POST': # 如果表单被提交
        print 'post'
        print request.get_full_path()
        form = StudentForm(request.POST) # 获取Post表单数据
        print request.POST
        print form
        if form.is_valid(): # 验证表单
            print form.cleaned_data['name']
            test = form.save(commit=False)
            test.save()
            form.save()
            # return HttpResponseRedirect('/campus') # 跳转
            return HttpResponse('success')
        else:
            form = Student() #获得表单对象
            print 'is not valid'

    else:
        print 'request not belong to POST'
        # logging.debug('request not belong to POST')

    return HttpResponse('error')

def info(request):
    students = Student.objects.all()
    t = loader.get_template("info.html")
    c = Context({'students': students})
    return HttpResponse(t.render(c))

def delete(request):
    if 'delete' in request.GET:
        key = request.GET['delete']
        print 'key: ' + key
        seats = Student.objects.get(email=key).delete()

    students = Student.objects.all()
    t = loader.get_template("info.html")
    c = Context({'students': students})
    return HttpResponse(t.render(c))