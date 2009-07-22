# Create your views here.


from django.shortcuts import render_to_response, get_object_or_404

def standard_plot(request, mapping_id):
    
    # get mapping out the database here...
    
    return render_to_response('standardview.html', 
        {'time_series_id': 'uMWN-IUdTBGLKc4VJmHoQA'})
    
    
    
