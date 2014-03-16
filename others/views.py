from cStringIO import StringIO
import csv
import datetime
import os
from django.contrib.gis.feeds import Feed
from django.http.response import HttpResponse
from django.shortcuts import render


# Create your views here.
from django.utils.feedgenerator import Atom1Feed
from reportlab.pdfgen import canvas
from djangobook import settings


def temp_home(request):
    return HttpResponse("It is others home")


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


#chapter 13 Generating PDFs install reportlab lib before run this function
def hello_pdf(request):
    # Create the HttpResponse object with the appropriate PDF headers.
    response = HttpResponse(mimetype='application/pdf')
    response['Content-Disposition'] = 'attachment; filename=hello.pdf'

    # Create the PDF object, using the response object as its "file."
    p = canvas.Canvas(response)

    # Draw things on the PDF. Here's where the PDF generation happens.
    # See the ReportLab documentation for the full list of functionality.
    p.drawString(100, 100, "Hello world.")

    # Close the PDF object cleanly, and we're done.
    p.showPage()
    p.save()
    return response


#chapter 13 complex pdf
def hello_pdf_com(request):
    # Create the HttpResponse object with the appropriate PDF headers.
    response = HttpResponse(mimetype='application/pdf')
    response['Content-Disposition'] = 'attachment; filename=hello.pdf'

    temp = StringIO()

    # Create the PDF object, using the StringIO object as its "file."
    p = canvas.Canvas(temp)

    # Draw things on the PDF. Here's where the PDF generation happens.
    # See the ReportLab documentation for the full list of functionality.
    p.drawString(100, 100, "Hello world.")

    # Close the PDF object cleanly.
    p.showPage()
    p.save()

    # Get the value of the StringIO buffer and write it to the response.
    response.write(temp.getvalue())
    return response


class LatestEntries(Feed):
    title = "My Blog"
    link = "/archive/"
    description = "The latest news about stuff."

    def items(self):
        return ['1', '2', '3']

    def item_title(self, item):
        return 'gtitle'

    def item_description(self, item):
        return 'gcreate'

    def item_link(self, item):
        return '/gtest' #reverse('news-item', args=[item.pk])


#Atom
class AtomSiteNewsFeed(LatestEntries):
    feed_type = Atom1Feed
    subtitle = LatestEntries.description


#more complex feed
# class TagFeed(Feed):
#     def get_object(self, bits):
#         # In case of "/feeds/tags/cats/dogs/mice/", or other such
#         # clutter, check that bits has only one member.
#         if len(bits) != 1:
#             raise ObjectDoesNotExist
#         return Tag.objects.get(tag=bits[0])
#
#     def title(self, obj):
#         return "My Blog: Entries tagged with %s" % obj.tag
#
#     def link(self, obj):
#         return obj.get_absolute_url()
#
#     def description(self, obj):
#         return "Entries tagged with %s" % obj.tag
#
#     def items(self, obj):
#         entries = Entry.objects.filter(tags__id__exact=obj.id)
#         return entries.order_by('-pub_date')[:30]


def test_len(request, bits):
    split_list = bits.split('/')
    strtemp = "bit len " + str(len(split_list)) + " " + split_list[0]
    return HttpResponse(strtemp)


#chapter14 cookies
def show_color(request):
    if "favorite_color" in request.COOKIES:
        return HttpResponse("Your favorite color is %s" %
                            request.COOKIES["favorite_color"])
    else:
        return HttpResponse("You don't have a favorite color.")


def set_color(request):
    if "favorite_color" in request.GET:

        # Create an HttpResponse object...
        response = HttpResponse("Your favorite color is now %s" %
                                request.GET["favorite_color"])

        # ... and set a cookie on the response
        response.set_cookie("favorite_color",
                            request.GET["favorite_color"])

        return response

    else:
        return HttpResponse("You didn't give a favorite color.")


#chapter14 session
def show_color_session(request):
    if "favorite_color" in request.session:
        temp = "Your favorite color is %s" % request.session["favorite_color"]
        del request.session["favorite_color"]
        return HttpResponse(temp)
    else:
        return HttpResponse("You don't have a favorite color.")


def set_color_session(request):
    if "favorite_color" in request.GET:

        # Create an HttpResponse object...
        response = HttpResponse("Your favorite color is now %s" %
                                request.GET["favorite_color"])

        # ... and set a session on the response
        request.session["favorite_color"] = request.GET["favorite_color"]

        return response

    else:
        return HttpResponse("You didn't give a favorite color.")