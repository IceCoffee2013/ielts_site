from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'ielts.views.show', name='home'),
    # url(r'^blog/', include('blog.urls')),
    # url(r'^show/', include(views.show)),
    url(r'^subscribe/', 'ielts.views.subscribe'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^search/', 'ielts.views.search'),
    url(r'^12306/', 'train.views.show'),
    url(r'^search12306/', 'train.views.search'),
    url(r'^photo/', 'photo_grasp.views.home'),
    url(r'^searchphoto/', 'photo_grasp.views.search'),
    # url(r'^phone/', '')

)
