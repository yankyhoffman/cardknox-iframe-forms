from django import forms
from django.shortcuts import render


class PaymentForm(forms.Form):
    card_sut = forms.CharField()
    cvv_sut = forms.CharField()
    zip = forms.CharField()
    name = forms.CharField()
    amount = forms.CharField()
    details = forms.CharField()


def index(request):
    received_form = PaymentForm(request.POST)
    return render(request, 'index.html', {'received': received_form})
