from django import forms
from .models import Activity
class ActivityForm(forms.ModelForm):
    name = forms.CharField(max_length=100, help_text="Please enter the activity name.")
    description = forms.CharField(max_length=100, help_text="Please enter the activity name.")
    author = forms.CharField(max_length=50, help_text="Please enter the activity name.")
    create_date = forms.DateField()
# An inline class to provide additional information on the form.
    class Meta:
    # Provide an association between the ModelForm and a model
        model = Activity
        fields = ('name',)