
from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.utils.encoding import DjangoUnicodeDecodeError
from django.contrib.auth.models import User
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django import forms


from codatimetric.mapping.models import RemoteToken

from codatimetric.mapping.oauthwrapper import *
from codatimetric.mapping.coda import *

##############################################################################
#        
@login_required
def coda_pre_auth(request):
    
    return render_to_response('preauth.html', 
        {},
        context_instance=RequestContext(request))
    
#
##############################################################################


##############################################################################
#        
def coda_auth(request):
    
    # when we get here we start the auth process with the CODA Server
    request_token = get_request_token()
    
    if request_token != None:
        
        request = 'oauth_token=%s&oauth_callback=%s' % (request_token.key, 
                urllib.quote('http://%s/auth/done/' % request.META['HTTP_HOST']))
        
        return HttpResponseRedirect("%soauth/authorize/?%s" % (settings.CODA_SERVER, request))
    else:
        return render_to_response('preauthfail.html',
            {},
            context_instance=RequestContext(request))   
#
##############################################################################


##############################################################################
#        
def coda_auth_done(request):
    
    # we get the request token passed as a GET param
    token_key = request.GET['oauth_token']
    
    request_token = get_object_or_404(RequestToken, key=token_key)
    
    access_token = get_access_token(request.user, request_token)
    
    if access_token:
        return render_to_response('authwin.html', {},
            context_instance=RequestContext(request))
    else:
        return render_to_response('preauthfail.html',
            {},
            context_instance=RequestContext(request))   
#
##############################################################################