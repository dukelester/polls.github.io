# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
# from .models import Question
# Register your models here.
from .models import Question, Choice, DukeLester


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date']}),
    ]


admin.site.register(Question, QuestionAdmin)


class ChoiceInline(admin.StackedInline):
    model = Choice
    extra = 3


admin.site.register(Choice)

admin.site.register(DukeLester)
