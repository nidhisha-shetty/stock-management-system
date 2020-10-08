from django import forms
from .models import Stock
class Stockf(forms.ModelForm):
	class Meta:
		model = Stock
		fields=[
			'product_name',
    		'no_of_items_left'
		]