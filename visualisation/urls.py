
from django.conf.urls.defaults import *

# rendering for the main page
urlpatterns = patterns(
    'visualisation.views',
    (r'^plot/(\d+)/standard/$',   'standard_plot'),
)