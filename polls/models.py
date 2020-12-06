# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
# Create your models here.
from django.db.models import CASCADE


class Question(models.Model):
    def __str__(self):
        return self.question_text

    question_text = models.CharField(max_length=200)
    pub_date = models.DateField('The date of publish')


class Choice(models.Model):

    def __str__(self):
        return self.choice_text

    question = models.ForeignKey(Question, on_delete=CASCADE)
    choice_text = models.CharField(max_length=200)
    vote = models.IntegerField(default=0)

    # def was_published_recently(self):
    #     return self.pub_date >= timezone.now()
    # datetime.timedelta(days=1)


class DukeLester(models.Model):
    FirstName = models.CharField(max_length=200)
    MiddleName = models.CharField(max_length=200)
    LastName = models.CharField(max_length=200)
    age = models.IntegerField(default=0)
    gender = models.CharField(max_length=45)
    status = models.CharField(max_length=45)
