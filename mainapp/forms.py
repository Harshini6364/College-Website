from django import forms

class EmailForm(forms.Form):
    BRANCH_CHOICES = [
        ('cse', 'CSE'),
        ('ece', 'ECE'),
        ('eee', 'EEE'),
        # ('mech', 'Mechanical'),
        # ('civil', 'Civil'),
    ]
    subject = forms.CharField(max_length=100)
    branch = forms.ChoiceField(choices=BRANCH_CHOICES)
    message = forms.CharField(widget=forms.Textarea)