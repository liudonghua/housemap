from django.conf.urls import url, include
from django.contrib import admin

from map.views import getRange

admin.autodiscover()

urlpatterns = [
    # Examples:
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', admin.site.urls),
    url(r'^getRange/',getRange,name='getRange')
]
    