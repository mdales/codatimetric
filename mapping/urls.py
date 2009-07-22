
from django.conf.urls.defaults import *

# rendering for the main page
urlpatterns = patterns(
    'mapping.views',
    (r'^$',                                         'home'),
)