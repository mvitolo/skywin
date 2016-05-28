from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.utils.translation import activate


def change_lang_en(request):
    activate('en')
    return HttpResponseRedirect(reverse('home'))


def change_lang_it(request):
    activate('it')
    return HttpResponseRedirect(reverse('home'))
