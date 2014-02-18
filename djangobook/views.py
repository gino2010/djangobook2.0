from django.shortcuts import render
from django.template import Context
from django.template.loader import get_template
from django.http import HttpResponse, Http404
import datetime


#chapter03
def hello(request):
    return HttpResponse("Hello world")


#chapter03
def my_homepage_view(request):
    return HttpResponse("Home Page")


#chapter03
# def current_datetime(request):
#     now = datetime.datetime.now()
#     html = "<html><body>It is now %s.</body></html>" % now
#     return HttpResponse(html)


#chapter04
def current_datetime(request):
    now = datetime.datetime.now()
    t = get_template('current_datetime.html')
    html = t.render(Context({'current_date': now}))
    return HttpResponse(html)


#chapter03
def hours_ahead(request, offset):
    try:
        offset = int(offset)
    except ValueError:
        raise Http404()
    dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
    #assert False #break point for debug
    # html = "<html><body>In %s hour(s), it will be %s.</body></html>" % (offset, dt)
    # return HttpResponse(html)
    # chapter04
    t = get_template('hours_ahead.html')
    html = t.render(Context({'hour_offset ': offset, 'next_time': dt}))
    return HttpResponse(html)


#chapter07
def display_meta(request):
    values = request.META.items()
    values.sort()
    # html = []
    # for k, v in values:
    #     html.append('<tr><td>%s</td><td>%s</td></tr>' % (k, v))
    # return HttpResponse('<table>%s</table>' % '\n'.join(html))
    return render(request, 'meta.html', {'values': values})


def debug(request):
    return None


def display_zip(request):
    return render(request, 'global.html')