from django.db import models, connection


# Create your models here.
class Publisher(models.Model):
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=60)
    state_province = models.CharField(max_length=30)
    country = models.CharField(max_length=50)
    website = models.URLField()

    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ['name']


class Author(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=40)
    email = models.EmailField('e-mail', blank=True) #verbose_name = 'e-mail'

    def __unicode__(self):
        return u'%s %s' % (self.first_name, self.last_name)


#chapter10 model manager
class BookManager(models.Manager):
    def title_count(self, keyword):
        return self.filter(title__icontains=keyword).count()


class DahlBookManager(models.Manager):
    def get_query_set(self):
        return super(DahlBookManager, self).get_query_set().filter(authors=1)


class Book(models.Model):
    title = models.CharField(max_length=100)
    authors = models.ManyToManyField(Author)
    publisher = models.ForeignKey(Publisher)
    publication_date = models.DateField()
    #chapter10 add new field
    num_pages = models.IntegerField(blank=True, default=0)

    #chapter10
    objects = BookManager()
    dahl_objects = DahlBookManager()

    def __unicode__(self):
        return self.title


#chapter 10
class MaleManager(models.Manager):
    def get_query_set(self):
        return super(MaleManager, self).get_query_set().filter(sex='M')


#chapter 10
class FemaleManager(models.Manager):
    def get_query_set(self):
        return super(FemaleManager, self).get_query_set().filter(sex='F')


#chapter 10
class PersonManager(models.Manager):

    def first_names(self, last_name):
        cursor = connection.cursor()
        cursor.execute("""
            SELECT DISTINCT first_name
            FROM books_person
            WHERE last_name = %s""", [last_name])
        return [row[0] for row in cursor.fetchone()]


#chapter 10
class Person(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    sex = models.CharField(max_length=1, choices=(('M', 'Male'), ('F', 'Female')))
    birth_date = models.DateField()
    address = models.CharField(max_length=100, blank=True)
    city = models.CharField(max_length=50, blank=True)

    objects = models.Manager()
    person = PersonManager()
    people = models.Manager()
    men = MaleManager()
    women = FemaleManager()

    def __unicode__(self):
        return u'%s %s' % (self.first_name, self.last_name)

    def baby_boomer_status(self):
        # "Returns the person's baby-boomer status."
        import datetime
        if datetime.date(1945, 8, 1) <= self.birth_date <= datetime.date(1964, 12, 31):
            return "Baby boomer"
        if self.birth_date < datetime.date(1945, 8, 1):
            return "Pre-boomer"
        return "Post-boomer"

    def _get_full_name(self):
        # "Returns the person's full name."
        return u'%s %s' % (self.first_name, self.last_name)
    full_name = property(_get_full_name)