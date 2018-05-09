from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.

class Post(models.Model):

    category = (

        ('Broken', 'Broken'),
        ('Danger', 'Danger'),
        ('Incident', 'Incident'),
        ('Info', 'Info'),
        ('Warning', 'Warning'),

    )

    tst_choice = (
        ('1', '1'),
        ('2', '2'),
    )

    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=90)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now())
    published_date = models.DateTimeField(blank=True, null=True)
    category = models.CharField(choices=category, max_length=40, default=1)
    tst = models.CharField(choices=tst_choice, max_length=2, default="")

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title