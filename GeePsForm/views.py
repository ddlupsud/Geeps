from django.shortcuts import render

from .utils import sendMail
from .forms import GeepsForm

# Create your views here.

def form(request, language):
	return render(request, 'form/' + language + '/form.html')
	
def submit(request, language):
	if request.method == 'POST':
		form = GeepsForm(request.POST)
		
		if form.is_valid():
			sendMail()
			return render(request, 'form/' + language + '/sent.html')
		else: 
			return render(request, 'form/' + language + '/form.html')
	else:
		return render(request, 'form/' + language + '/form.html')
