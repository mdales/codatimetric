# Create your views here.

from django.shortcuts import render_to_response, get_object_or_404

from mapping.models import Graph

def standard_plot(request, mapping_id):
    
    # get mapping out the database here...
    g = Graph.objects.get(pk=int(mapping_id))
    return render_to_response('standardview.html', 
        {'time_series_id': g.timetric_id})
    
    
    
