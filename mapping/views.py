

from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.utils.encoding import DjangoUnicodeDecodeError
from django.contrib.auth.models import User
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django import forms


@login_required
def home(request):
    
    return render_to_response("home.html", {}, 
        context_instance=RequestContext(request))