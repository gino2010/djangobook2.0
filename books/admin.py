from django.contrib import admin
#chapter06
# Register your models here.
from books.models import Publisher, Author, Book, Person, Group


class AuthorAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email')
    search_fields = ('first_name', 'last_name')


class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'publisher', 'publication_date')
    list_filter = ('publication_date',)
    date_hierarchy = 'publication_date'
    ordering = ('-publication_date',)
    # fields = ('title', 'authors', 'publisher', 'publication_date') #show detial fields
    filter_horizontal = ('authors',) #in change page
    raw_id_fields = ('publisher',)


class PersonAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'sex')

admin.site.register(Publisher)
admin.site.register(Person, PersonAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Book, BookAdmin)
admin.site.register(Group)