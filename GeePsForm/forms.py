from django import forms

class GeepsForm(forms.Form):
	name = forms.CharField(),
	first_name = forms.CharField(),
	email = forms.EmailField(),
	phone = forms.RegexField(r'^((\+|00)33\s?|0)[67](\s?\d{2}){4}$'),
	office = forms.CharField(),
	building = forms.ChoiceField(), # TODO: validation
	release = forms.ChoiceField(), # same
	os = forms.ChoiceField(), # same
	hostid = forms.RegexField(r'^(([0-9a-zA-Z]{2})[-|:]){5}\2$'),
	language = forms.CharField(),