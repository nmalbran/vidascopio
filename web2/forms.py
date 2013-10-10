# -*- coding: utf-8 -*-
from django import forms

class ContactoForm(forms.Form):
    nombre = forms.CharField()
    mail = forms.EmailField()
    telefono = forms.CharField(label='Teléfono')
    mensaje = forms.CharField(widget=forms.Textarea, label='Mensaje')