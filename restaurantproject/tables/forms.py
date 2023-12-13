from django import forms
from django.utils import timezone
from .models import Tables, Tables_orders



class OrderForm(forms.ModelForm):

    class Meta:
        model = Tables_orders
        fields = ('date',)

        widgets = {
            'date': forms.DateInput(attrs={'min': timezone.now().strftime('%Y-%m-%d'), 'type':'date'})
        }

    def clean(self):
        if self.cleaned_data['date'] < timezone.now().date():
            raise forms.ValidationError("Виберіть дату у майбутньому.")



