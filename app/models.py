from django.db import models
from django.db.models.signals import pre_save
import re
from django.contrib.auth.models import User

class Bounty(models.Model):
    user = models.ForeignKey(User, blank=True, null=True)
    title = models.TextField(max_length=255)
    description = models.TextField()
    amount = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

class Category(models.Model):
    parent = models.ForeignKey('Category', blank=True, null=True)
    title = models.CharField(max_length=255)
    seen = models.BigIntegerField()
    suggested = models.BigIntegerField()
    used = models.BigIntegerField()

class BountyCategory(models.Model):
    bounty = models.ForeignKey(Bounty)
    category = models.ForeignKey(Category)
    created = models.DateTimeField(auto_now_add=True)
