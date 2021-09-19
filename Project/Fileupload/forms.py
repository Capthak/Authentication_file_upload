from django import forms
from .models import Document

class DocumentMdelForm(forms.ModelForm):
    class Meta:
        model=Document
        fields=['description','document']