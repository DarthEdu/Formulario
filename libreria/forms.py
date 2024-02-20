from django import forms
from django.forms import ModelForm
from .models import Venue


# Create a venue forms

class VenueForm(ModelForm):
    class Meta:
        model = Venue
        fields = "__all__"
