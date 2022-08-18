from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .models import Shortener
from .forms import ShortenerForm


def home_view(request):
    template = 'home.html'
    context={}

    #Empty Form intialize
    #context['form'] = ShortenerForm()
    form = ShortenerForm
    context ={
        'form': form
    }
    if request.method == 'GET':
        return render(request=request, template_name=template, context=context)

    elif request.method == 'POST':
        used_form = ShortenerForm(request.POST)
        if used_form.is_valid():
            shortened_object = used_form.save()
            new_url = request.build_absolute_uri('/') + shortened_object.short_url
            long_url = shortened_object.long_url
            context['new_url']  = new_url
            context['long_url'] = long_url
            return render(request, template, context)
        context['errors'] = used_form.errors
        return render(request=request, template_name=template, context=context)


def redirect_url_view(request, shortened_part):

    try:
        shortener = Shortener.objects.get(short_url=shortened_part)
        shortener.times_followed += 1        
        shortener.save()
        return HttpResponseRedirect(shortener.long_url)
        
    except:
        raise HttpResponse('Sorry this link is broken :(', status=404)