
from django.conf.urls.defaults import *

# rendering for the main page
urlpatterns = patterns(
    'visualisation.views',
    url(r'^plot/(\d+)/standard/$',   'standard_plot', name="standard_plot"),
)