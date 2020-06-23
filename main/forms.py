from django.contrib.admin import forms
from .models import Stock

class ChangeCategoryForm(forms.Form):
    _selected_action = forms.CharField(widget=forms.MultipleHiddenInput)
    category = forms.ModelChoiceField(queryset=Stock.objects.all(),
                                      label=u'Основная категория')