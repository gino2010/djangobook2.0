from django.db import models


# Create your models here.
class Ren(models.Model):
    name = models.CharField(max_length=128)

    # On Python 3: def __str__(self):
    def __unicode__(self):
        return self.name


class Zu(models.Model):
    name = models.CharField(max_length=128)
    members = models.ManyToManyField(Ren, through='Membership')

    # On Python 3: def __str__(self):
    def __unicode__(self):
        return self.name


class Membership(models.Model):
    person = models.ForeignKey(Ren)
    group = models.ForeignKey(Zu)
    date_joined = models.DateField()
    invite_reason = models.CharField(max_length=64)