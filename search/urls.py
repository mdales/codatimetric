
from django.conf.urls.defaults import *

# rendering for the main page
urlpatterns = patterns(
    'search.views',
    (r'^search/$',                              'search'),
)