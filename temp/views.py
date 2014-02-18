import datetime
from django.http.response import HttpResponse
from django.shortcuts import render


# Create your views here.
def temp_home(request):
    return HttpResponse("It is temp home")


def ordering(request):
    person_name = 'Gino'
    company = 'Vertechs'
    item_list = ['android', 'cloud', 'python']
    ship_date = datetime.date(2014, 4, 2)
    ordered_warranty = False
    # return render(request, 'ordering.html', {'person_name': person_name, 'company': company, 'ship_date': ship_date,
    #                                          'item_list': item_list, 'ordered_warranty': ordered_warranty})
    return render(request, 'ordering.html', locals())


def navtemp(request, title, current):
    return render(request, 'navtemp.html', {'title': title, 'current_section': current})


# chapter08
def foobar_view(request, template_name):
    m_list = ['1', '2']
    return render(request, template_name, {'m_list': m_list})


def my_view(request, month, day):
    return render(request, 'mydate.html', {'month': month, 'day': day})


def day_archive(request, year, month, day):
    date = datetime.date(int(year), int(month), int(day))
    return HttpResponse("date is %s" % date)


# chapter09 Creating a Template Library
def filter_view(request):
    return render(request, 'book_snippet.html', {'somevariable': 'Django Book'})