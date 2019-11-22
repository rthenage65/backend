from django import forms

class CommentForm(forms.Form):
    name = forms.CharField(max_length=100)
    comment = forms.CharField(max_length=1000, widget=forms.Textarea)

    def clean(self):
        cleaned_data = super().clean()
        name = cleaned_data.get('name')
        if 'kyler' in name.lower():
            raise forms.ValidationError('Your name cannot be pronounced')


