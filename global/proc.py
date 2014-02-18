__author__ = 'Gino'


#customer Context Processors
def custom_proc(request):
    return {
        'home_link': '/',
        'home_title': 'home',
        'user': request.user,
        'ip_address': request.META['REMOTE_ADDR']
    }
