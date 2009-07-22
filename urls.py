from django.conf.urls.defaults import *

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    (r'^', include('codatimetric.mapping.urls')),
    (r'^admin/(.*)', admin.site.root),
)


urlpatterns += patterns(
    '',
    (r'^accounts/login/$', 'django.contrib.auth.views.login'),
    (r'^accounts/logout/$', 'django.contrib.auth.views.logout'),
    (r'^accounts/pwchange/$', 'django.contrib.auth.views.password_change'),
    (r'^accounts/password_reset/done/$', 'django.contrib.auth.views.password_reset_done'),
    (r'^accounts/reset/(?P<uidb36>[0-9A-Za-z]+)-(?P<token>.+)/$', 'django.contrib.auth.views.password_reset_confirm'),
    (r'^accounts/reset/done/$', 'django.contrib.auth.views.password_reset_complete'),
)