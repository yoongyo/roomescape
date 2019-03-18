from django.urls import re_path
from . import views

urlpatterns = [
    re_path(r'^$', views.theme, name='theme'),
    re_path(r'^info/$', views.theme_info, name='theme_info'),
    re_path(r'^(?P<date>(19|20)\d{2}-(0[1-9]|1[012])-(0[1-9]|[12][0-9]|3[0-1]))/$',
            views.theme_list, name='theme_list'),
    re_path(r'^(?P<date>(19|20)\d{2}-(0[1-9]|1[012])-(0[1-9]|[12][0-9]|3[0-1]))/(?P<theme>[\w|\W]+)/'
            r'(?P<time>[\w|\W]+)/complete/$', views.booking_complete, name='booking_complete'),
    re_path(r'^(?P<date>(19|20)\d{2}-(0[1-9]|1[012])-(0[1-9]|[12][0-9]|3[0-1]))/(?P<theme>[\w|\W]+)/'
            r'(?P<time>[\w|\W]+)/$', views.booking_detail, name='booking_detail'),
    re_path(r'^(?P<date>(19|20)\d{2}-(0[1-9]|1[012])-(0[1-9]|[12][0-9]|3[0-1]))/(?P<theme>[\w|\W]+)/$',
            views.theme_booking, name='theme_booking'),
]
