from django.shortcuts import render_to_response
from django.template import RequestContext


# ===========================================================================
# HOME
# ===========================================================================
def home(request, template_name="bot/home.html"):
    return render_to_response(template_name, {
        'session': request.session.keys(),
    }, context_instance=RequestContext(request))
