from django import forms

class FilesForm(forms.Form):
    files = forms.FileField(widget=forms.ClearableFileInput(attrs = {'class': 'form__file-input-btn t1', 'name': 'files', 'multiple': 'true', 'id': 'inp'}))