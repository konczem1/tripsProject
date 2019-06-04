from django.db import models
from django.utils import timezone


# Create your models here.
class User(models.Model):
    firstName = models.CharField(max_length=20)
    lastName = models.CharField(max_length=20)
    dateOfBirth = models.DateField()
    dateOfJoining = models.DateTimeField(default=timezone.now)
    country = models.CharField(max_length=20)
    email = models.EmailField()
    password = models.CharField(max_length=20)

    class Meta:
        ordering = ('lastName', 'firstName',)

    def __str__(self):
        return self.email


class Photo(models.Model):
    filename = models.CharField(max_length=200)
    latitude = models.FloatField(null=True)
    longitude = models.FloatField(null=True)
    #tags = ArrayField(models.CharField(max_length=20), null=True)
    owner = models.ForeignKey(User, related_name='user_owner_photo', on_delete=models.CASCADE)
    #shared = models.ManyToManyField(User, related_name='user_shared_photo', blank=True)

    class Meta:
        ordering = ('filename',)

    def __str__(self):
        return self.filename

