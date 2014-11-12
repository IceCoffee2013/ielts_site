import os
import sys

sys.path.append('/var/www/ielts_site/ielts_site')

os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()