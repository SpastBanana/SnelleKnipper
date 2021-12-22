from django.forms import ModelForm
from .models import newsBlocks

class newsForm(ModelForm):
    class Meta:
        model = newsBlocks
        fields = '__all__'
