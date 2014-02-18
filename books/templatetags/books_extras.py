from books.models import Book
from django import template
# chapter09 Inclusion Tags
__author__ = 'Gino'

register = template.Library()


@register.inclusion_tag('book_snippet.html')
def books_for_author(author):
    books = Book.objects.filter(authors__id=author.id)
    return {'books': books}

register.inclusion_tag('book_snippet.html')(books_for_author)


@register.inclusion_tag('link.html', takes_context=True)
def jump_link(context):
    return {
        'link': context['home_link'],
        'title': context['home_title'],
    }