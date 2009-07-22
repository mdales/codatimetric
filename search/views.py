from __future__ import absolute_import

import simplejson
import httplib2

from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.utils.encoding import DjangoUnicodeDecodeError
from django.contrib.auth.models import User
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django import forms

from .forms import SearchForm

@login_required
def search(request):
    if not request.GET:
        f = SearchForm()
        series = None
    else:
        f = SearchForm(request.GET)
        if f.is_valid():
            print "Retrieving search results for title: ", f.cleaned_data["title"]
            h = httplib2.Http(".cache")
            requrl = "http://timetric.com/search/results.fat.json?q="+ f.cleaned_data["title"]
            resp, content = h.request(requrl, "GET")
            series = simplejson.loads(content)["results"]
            print series
    return render_to_response("search.html", {"form":f, "series":series}, 
        context_instance=RequestContext(request))