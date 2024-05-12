from django import forms

class IndexForm(forms.Form):
    high_bp = forms.ChoiceField(
        label='High Blood Pressure',
        widget=forms.RadioSelect,
        choices=[
            ('N', 'No'),
            ('Y', 'Yes'),
        ],
        required=True,
    )
    high_chol = forms.ChoiceField(
        label='High Cholesterol',
        widget=forms.RadioSelect,
        choices=[
            ('N', 'No'),
            ('Y', 'Yes'),
        ],
        required=True,
    )
    chol_check = forms.ChoiceField(
        label='Checked cholesterol in last 5 years?',
        widget=forms.RadioSelect,
        choices=[
            ('N', 'No'),
            ('Y', 'Yes'),
        ],
        required=True,
    )
    bmi = forms.IntegerField(
        label='BMI',
        required=True,
        min_value=9,
        max_value=100,
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
        min_value=1,
        max_value=120,
    )
