from django import forms
from .models import Chit

class ChitForm(forms.ModelForm):
	class Meta:
		model = Chit
		fields = ('base_date', 'card', 'amount', 'place', 'order_user', 'number_of_user', 'list_of_user', 'meal_type')