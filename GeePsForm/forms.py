from django import forms

class GeepsForm(forms.Form):
	name = forms.CharField(),
	first_name = forms.CharField(),
	email = forms.EmailField(),
	phone = forms.RegexField(r'^((\+|00)33\s?|0)[67](\s?\d{2}){4}$'),
	office = forms.CharField(),
	building = forms.ChoiceField(),
	release = forms.ChoiceField(),
	os = forms.ChoiceField(),
	hostid = forms.RegexField(r'^(([0-9a-zA-Z]{2})[-|:]){5}\2$'),
	language = forms.CharField(),
	
class LanguageForm(forms.Form):
	language = forms.ChoiceField(),