import datetime

from django.core.mail import send_mail
from django.conf import settings

from io import BytesIO

from reportlab.pdfgen import canvas

from .forms import GeepsForm

def sendMail(form):
	sender = getattr(settings, "EMAIL_HOST_USER", None)
	release = form.cleaned_data['release']
	os = form.cleaned_data['os']
	
	# envoi mail à cri@geeps
	send_mail(
		'Activation Licence Matlab',
		'Demande d\'activation de Matlab' + release + ' de ' + form.cleaned_data['first_name'] + ' ' +
		form.cleaned_data['name'] + ' pour le systeme ' + os + '.',
		sender,
		# "cri@geeps.centralesupelec.fr",
		["diego.daninthe@u-psud.fr"],
		fail_silently=False,
	)
	# TODO: add csv and pdf
	
	subject = None
	body = None
	
	if (form.cleaned_data['language'] == 'en'):
		subject = "Licence Matlab activation request"
		body = 'Your Matlab "MatlabRelease" request activation for your "OperatingSystem" operating system was well taken into' 
		+ 'account.\n\nGeePs\'CRI'
	else:
		subject = "Demande d'activation de la licence Matlab"
		body = "Votre demande d'activation de Matlab " + release + " a bien ete prise en compte pour votre systeme " 
		+ os + ".\n\nLe CRI du GeePs"
		
	# acquittement
	send_mail(subject, body, sender, [form.cleaned_data['email']], fail_silently=False)
	
def generateCSV(form):
	firstName = form.cleaned_data['first_name']
	name = form.cleaned_data['name']
	email = form.cleaned_data['email']
	phone = form.cleaned_data['phone']
	release = form.cleaned_data['release']
	os = form.cleaned_data['os']
	office = form.cleaned_data['office']
	building = form.cleaned_data['building']
	hostid = form.cleaned_data['hostid']
	
	date = datetime.date.today()
	filename = "matlab-" + release + "-" + firstName + "_" + name + "-" + date + ".pdf"
	
	return
	
def generatePDF(form):
	# liste champ-valeur
	# date
	# logo
	# titre
	firstName = form.cleaned_data['first_name']
	name = form.cleaned_data['name']
	email = form.cleaned_data['email']
	phone = form.cleaned_data['phone']
	release = form.cleaned_data['release']
	os = form.cleaned_data['os']
	office = form.cleaned_data['office']
	building = form.cleaned_data['building']
	hostid = form.cleaned_data['hostid']
	
	date = datetime.date.today()
	filename = "matlab-" + release + "-" + firstName + "_" + name + "-" + date + ".pdf"
	
	buffer = BytesIO()
	p = canvas.Canvas(buffer)
	
	#p.drawString(100, 100, )
