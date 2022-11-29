import json
# for older versions (and using python < 2.7)
#from django.utils import simplejson
# and change the json.dumps for simplejson.dumps
from django.http import HttpResponse

def home(requst):

    responseData = {
        'Message': 'Hello World!'
    }
    return HttpResponse(json.dumps(responseData), content_type="application/json")