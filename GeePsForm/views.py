from django.shortcuts import render, redirect

from .utils import sendMail
from .forms import GeepsForm, LanguageForm

# Create your views here.

def changeLanguage(request):
	"""Load template on language change"""
	if request.method == 'POST':
		form = LanguageForm(request.POST)
		if form.is_valid():
			language = form.data.get('language')
			return redirect('/' + language)
		else:
			return redirect('/')

def form(request, language):
	return render(request, 'form/' + language + '/form.html')
	
def submit(request, language):
	if request.method == 'POST':
		form = GeepsForm(request.POST)
		
		if form.is_valid():
			sendMail(form)
			return render(request, 'form/' + language + '/sent.html')
		else: 
			return render(request, 'form/' + language + '/form.html')
	else:
		return render(request, 'form/' + language + '/form.html')
