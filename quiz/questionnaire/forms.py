# This Python file uses the following encoding: utf-8

import os
from django import forms
from django.conf import settings
from django.http import HttpResponse, Http404
from dataclasses import dataclass



class QuestionForm(forms.Form):
    CHOICES = {
        "1": "Нет",
        "2": "Скорее нет",
        "3": "Скорее да",
        "4": "Да"
    }


    def __init__(self, question):
        super().__init__()
        self.question = question
        self.choice_field = forms.MultipleChoiceField(label=self.question, widget=forms.RadioSelect, choices=QuestionForm.CHOICES)

    # checkbox_RSMOB = forms.BooleanField(label='RSMOB/VPN', required=False, disabled=False)
    # ip_ne = forms.CharField(label="IP NE", required=True, widget=forms.TextInput(attrs={"class":"myfield", "placeholder":"IP address of NE(172.21.x.x)..."}))
    # USERNAME = forms.CharField(label="USERNAME", required=True, widget=forms.TextInput(attrs={"class":"myfield", "placeholder":"username..."}))
    # checkbox_cookies = forms.BooleanField(label='PASSWORD(использовать cookies)', required=False, disabled=False)
    # PASSWORD = forms.CharField(label="PASSWORD", required=False, widget=forms.PasswordInput(attrs={"class":"myfield", "placeholder":"password..."}))
