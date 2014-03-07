import csv
import datetime
import os
from django.http.response import HttpResponse
from django.shortcuts import render


# Create your views here.
from djangobook import settings


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


# chapter13 Generating Non-HTML Content
def my_image(request):
    print(os.getcwd())
    image_data = open(os.path.join(settings.MEDIA_ROOT, "image/hb.png").replace('\\', '/'), "rb").read()
    return HttpResponse(image_data, mimetype="image/png")

# chapter 13 Producing CSV
UNRULY_PASSENGERS = [146, 184, 235, 200, 226, 251, 299, 273, 281, 304, 203]


def unruly_passengers_csv(request):
    # Create the HttpResponse object with the appropriate CSV header.
    response = HttpResponse(mimetype='text/csv')
    response['Content-Disposition'] = 'attachment; filename=unruly.csv'

    # Create the CSV writer using the HttpResponse as the "file."
    writer = csv.writer(response)
    writer.writerow(['Year', 'Unruly Airline Passengers'])
    for (year, num) in zip(range(1995, 2006), UNRULY_PASSENGERS):
        writer.writerow([year, num])

    return response