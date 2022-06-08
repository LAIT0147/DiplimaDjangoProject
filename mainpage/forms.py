from django import forms
from .models import ContactUs


class ContactUsForm(forms.ModelForm):
    name = forms.CharField(max_length=30, widget=forms.TextInput(attrs={
                                            'name': "name",
                                            'type': "text",
                                            'id': "name",
                                            'placeholder': "Your Name",
                                            'required': "required"
                                            }))
    email = forms.CharField(max_length=50, widget=forms.TextInput(attrs={
                                            'name': "email",
                                            'type': "text",
                                            'id': "email",
                                            'pattern': "[^ @]*@[^ @]*",
                                            'placeholder': "Your Email",
                                            'required': "required"
                                            }))
    subject = forms.CharField(max_length=100, widget=forms.TextInput(attrs={
                                                'name': "subject",
                                                'type': "text",
                                                'id': "subject",
                                                'placeholder': "Subject",
                                                'required': "required"
                                                }))
    message = forms.CharField(max_length=500, widget=forms.TextInput(attrs={
                                                'name': "message",
                                                'rows': "6",
                                                'id': "message",
                                                'placeholder': "Message",
                                                'required': "required"
                                                }))


    class Meta:
        model = ContactUs
        fields = ('name', 'email', 'subject', 'message')
