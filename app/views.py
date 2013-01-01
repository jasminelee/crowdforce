from django.shortcuts import render
import json
from django.http import HttpResponse, HttpResponseRedirect
from models import *

def render_json(data):
    return HttpResponse(json.dumps(data), mimetype="application/json")

def new_bounty(request):
    title = ''
    description = ''
    amount = ''
    if request.method == 'POST':
        success = False
        try:
            title = request.POST.get('title')
            description = request.POST.get('description')
            amount = request.POST.get('bounty')
            bounty = Bounty(title=title, description=description, amount=amount)
            bounty.save()
            success = True
        except:
            pass
        next_step = '/set_category/' + str(bounty.id) if success else ''

        if request.is_ajax():
            return render_json({'success': success, 'redirect': next_step})
        else:
            if success:
                return HttpResponseRedirect(next_step)
    return render(request, 'index.html', locals())

def set_category(request, id):
    return render(request, 'set_category.html')
