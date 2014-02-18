from django.core.mail import send_mail
from django.http.response import HttpResponseRedirect
from django.shortcuts import render


# Create your views here.
# chapter07
from books.forms import ContactForm
from books.models import Book


def search_form(request):
    return render(request, 'search_form.html')


# chapter07
def search(request):
    # assert False
    #-------------version 1 ---------------
    # if 'q' in request.GET:
    #     message = 'You search for: %r' % request.GET['q']
    # else:
    #     message = 'You submitted an empty form.'
    # return HttpResponse(message)
    #-------------version 2 ---------------
    # error = False
    # if 'q' in request.GET:
    #     q = request.GET['q']
    #     if not q:
    #         error = True
    #     elif len(q) > 20:
    #         error = True
    #     else:
    #         books = Book.objects.filter(title__icontains=q)
    #         return render(request, 'search_results.html', {'books': books, 'query': q})
    # # else:
    #     # return HttpResponse('Please submit a search term.')
    # return render(request, 'search_form.html', {'error': error})
    #---------------version 3 -----------------
    errors = []
    if 'q' in request.GET:
        q = request.GET['q']
        if not q:
            errors.append('Enter a search term.')
        elif len(q) > 20:
            errors.append('Please enter at most 20 characters.')
        else:
            books = Book.objects.filter(title__icontains=q)
            return render(request, 'search_results.html', {'books': books, 'query': q})
    return render(request, 'search_form.html', {'errors': errors})


# def contact(request):
#     errors = []
#     if request.method == 'POST':
#         if not request.POST.get('subject', ''):
#             errors.append('Enter a subject.')
#         if not request.POST.get('message', ''):
#             errors.append('Enter a message.')
#         if request.POST.get('email') and '@' not in request.POST['email']:
#             errors.append('Enter a valid e-mail address.')
#         if not errors:
#             send_mail(
#                 request.POST['subject'],
#                 request.POST['message'],
#                 request.POST.get('email', 'youmail@126.com'),
#                 ['yourmail@126.com'],
#                 True,
#             )
#             return HttpResponseRedirect('/books/thanks/')
#     return render(request, 'contact_form.html', {'errors': errors,
#         'subject': request.POST.get('subject', ''),
#         'message': request.POST.get('message', ''),
#         'email': request.POST.get('email', ''), })


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            send_mail(
                cd['subject'],
                cd['message'],
                cd.get('email', 'noreply@example.com'),
                ['siteowner@example.com'],
                True, #do not output error message for sending mail
            )
            return HttpResponseRedirect('/books/thanks/')
    else:
        form = ContactForm(initial={'subject': 'I love your site!'})
    return render(request, 'contact_form.html', {'form': form})


def thanks(request):
    return render(request, 'thanks.html')