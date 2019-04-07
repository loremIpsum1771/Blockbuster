# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.postgres.fields import JSONField
from django.db import models



    
class Genre(models.Model):
    name = models.CharField(max_length=120)


class Movie(models.Model):
    title = models.CharField(max_length=120)
    genre = JSONField(default = dict)
    numberInStock = models.IntegerField()
    dailyRentalRate = models.DecimalField( max_digits=5, decimal_places=1) 
    publishDate = models.DateTimeField(auto_now_add=True)
    liked = models.BooleanField()
