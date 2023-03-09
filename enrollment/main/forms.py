from django.forms import ModelForm
from . models import Hospitalization


class HospitalizationForm(ModelForm):
    
    class Meta:
        model = Hospitalization
        fields = "__all__"
