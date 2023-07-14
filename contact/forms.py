from django import forms

from .models import Contact

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['full_name', 'phone_number', 'email', 'message']

    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
        self.fields['full_name'].widget.attrs.update({
            'class': 'form-group',
            'placeholder': 'Your name'
        })
        self.fields['phone_number'].widget.attrs.update({
            'class': 'form-group',
            'placeholder': 'Phone number'
        })
        self.fields['email'].widget.attrs.update({
            'class': 'form-group',
            'placeholder': 'Email'
        })
        self.fields['message'].widget.attrs.update({
            'class': 'form-group',
            'placeholder': 'Message'
        })

    def clean(self):
        data = self.cleaned_data
        data['full_name'] = data['full_name'].title()
        data['message'] = data['message'].capitalize()
        return data