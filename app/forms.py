from django import forms

class IndexForm(forms.Form):
    high_bp = forms.BooleanField(
        label='High Blood Pressure',
        required=False,
    )
    high_chol = forms.BooleanField(
        label='High Cholesterol',
        required=False,
    )
    chol_check = forms.BooleanField(
        label='Checked cholesterol in last 5 years?',
        required=False,
    )
    bmi = forms.IntegerField(
        label='BMI',
        required=True,
    )
    gender = forms.ChoiceField(
        label='Gender',
        widget=forms.RadioSelect,
        choices=[
            ('M', 'Male'),
            ('F', 'Female'),
        ],
        required=True,
    )
    age = forms.IntegerField(
        label='Age',
        required=True,
    )
