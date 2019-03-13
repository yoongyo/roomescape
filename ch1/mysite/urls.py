from django.contrib import admin
from django.urls import re_path, include
from . import views

from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    re_path(r'^$', views.main, name='main'),
    re_path(r'^admin/', admin.site.urls),
    re_path(r'^theme/', include(('theme.urls', 'theme'), namespace='theme')),
    re_path(r'^information/', include(('information.urls', 'information'), namespace='information'))
]


urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)