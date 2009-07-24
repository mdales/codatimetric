
from django.core import urlresolvers
from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, Http404, HttpResponseNotAllowed
from django.utils.encoding import DjangoUnicodeDecodeError
from django.contrib.auth.models import User
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django import forms
                         
from models import Graph

from codatimetric.mapping.coda import add_new_timetric_source
from codatimetric.mapping.models import RemoteToken

@login_required
def home(request):
    graphs = Graph.objects.filter(user=request.user)
    return render_to_response("home.html", locals(), 
        context_instance=RequestContext(request))
        
@login_required
def graph(request):
    if request.method == "POST":
        
        graph = Graph()
        graph.title = request.POST["title"]
        graph.timetric_id = request.POST["id"]
        graph.user = request.user
        graph.save() # need this save to make sure there's an ID!
        
        token = RemoteToken.objects.filter(user=request.user)[0]
        source_uuid = add_new_timetric_source(token, graph.title, graph.id)

        graph.coda_source_id = source_uuid
        graph.save()
        
        
        return HttpResponseRedirect(urlresolvers.reverse("graph-view", args=[graph.pk,]))
    else:
        return HttpResponseNotAllowed(["POST",])
        
@login_required
def graph_view(request,pk):
    return render_to_response("graph.html", {"pk":pk}, 
        context_instance=RequestContext(request))    