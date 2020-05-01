from django.forms import ModelForm
from .models import Supporting

class SupportingForm(ModelForm):
  class Meta:
    model = Supporting
    fields = ['date', 'support']