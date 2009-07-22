
from django.conf.urls.defaults import *

# rendering for the main page
urlpatterns = patterns(
    'mapping.views',
    (r'^$',                                         'home'),
)

urlpatterns += patterns(
    'mapping.views',
    url(r'^graph/$', 'graph', name="graph"),
)

urlpatterns += patterns(
    'mapping.authviews',
    (r'^auth/$',                                    'coda_pre_auth'),
    (r'^auth/go/$',                                 'coda_auth'),
    (r'^auth/done/$',                               'coda_auth_done'),
)