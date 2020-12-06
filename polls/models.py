# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import datetime
from django.db import models
# Create your models here.
from django.db.models import CASCADE
from django.utils import timezone
from django.utils.datetime_safe import datetime
from datetime import datetime, timedelta


class Question(models.Model):
    def __str__(self):
        return self.question_text

    question_text = models.CharField(max_length=200)
    pub_date = models.DateField('The date of publish')

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now

        # futuredate = datetime.now() + timedelta(days=10)
        # return futuredate


def test_was_published_recently_with_old_question(self):
    """
    was_published_recently() returns False for questions whose pub_date
    is older than 1 day.
    """
    time = timezone.now() - datetime.timedelta(days=1, seconds=1)
    old_question = Question(pub_date=time)
    self.assertIs(old_question.was_published_recently(), False)


def test_was_published_recently_with_recent_question(self):
    """
    was_published_recently() returns True for questions whose pub_date
    is within the last day.
    """
    time = timezone.now() - datetime.timedelta(hours=23, minutes=59, seconds=59)
    recent_question = Question(pub_date=time)
    self.assertIs(recent_question.was_published_recently(), True)


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
