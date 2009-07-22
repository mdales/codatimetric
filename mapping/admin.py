from django.contrib import admin

from models import Graph

try:
    admin.site.register(Graph)
except admin.sites.AlreadyRegistered:
    pass
