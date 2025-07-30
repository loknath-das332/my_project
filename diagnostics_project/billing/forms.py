from django import forms
from .models import Patient , Test,Bill



class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = '__all__'

class TestForm(forms.ModelForm):
    class Meta:
        model = Test
        fields = '__all__'

class BillForm(forms.ModelForm):
    class Meta:
        model = Bill
        fields = ['patient', 'tests']
        widgets = {
            'patient': forms.Select(attrs={'class': 'form-control'}),
            'tests': forms.CheckboxSelectMultiple(),
        }