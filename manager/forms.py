from django import forms
from mainpage.models import Schedule


class ScheduleForm(forms.ModelForm):
    monday = forms.CharField(max_length=15, widget=(forms.TextInput(attrs={
                                                                    'type': 'name',
                                                                    'id': 'weekday',
                                                                    'plaseholder': ''
                                                                    })))
    tuesday = forms.CharField(max_length=15, widget=(forms.TextInput(attrs={
                                                                    'type': 'name',
                                                                    'id': 'weekday',
                                                                    'plaseholder': ''
                                                                    })))
    wednesday = forms.CharField(max_length=15, widget=(forms.TextInput(attrs={
                                                                    'type': 'name',
                                                                    'id': 'weekday',
                                                                    'plaseholder': ''
                                                                    })))
    thursday = forms.CharField(max_length=15, widget=(forms.TextInput(attrs={
                                                                    'type': 'name',
                                                                    'id': 'weekday',
                                                                    'plaseholder': ''
                                                                    })))
    friday = forms.CharField(max_length=15, widget=(forms.TextInput(attrs={
                                                                    'type': 'name',
                                                                    'id': 'weekday',
                                                                    'plaseholder': ''
                                                                    })))


    class Meta:
        model = Schedule
        fields = ('monday', 'tuesday', 'wednesday', 'thursday', 'friday')
