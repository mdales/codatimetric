from django.db import models

# Create your models here.

from django.contrib.auth.models import User

##############################################################################
#
class RequestToken(models.Model):
    """A token for the initial OAuth request. Stored in db as it needs to 
    survive past a call back invocation, but shouldn't last long."""
    
    key = models.CharField(max_length=255)
    secret = models.CharField(max_length=255)
    
    # keep a note of this, as failed callbacks may require GCing
    created = models.DateTimeField()
    
    def __unicode__(self):
        return "token %s/%s made at %s" % (self.key, self.secret, self.created)
#
##############################################################################


##############################################################################
#
class RemoteToken(models.Model):
    """This is the OAuth Access Token. In this system we associate it with 
    a particular user."""
    
    user = models.ForeignKey(User)
    
    key = models.CharField(max_length=255)
    secret = models.CharField(max_length=255)
    
    def __unicode__(self):
       return "token %s for user %s" % (self.key, self.user.username)
#
##############################################################################

class Graph(models.Model):
    user = models.ForeignKey(User)
    timetric_id = models.CharField(max_length=22)
    title = models.CharField(max_length=120)
    