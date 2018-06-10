import datetime
import csv

from django.core.mail import send_mail, EmailMessage
from django.conf import settings

from io import BytesIO, StringIO

from reportlab.lib.units import inch
from reportlab.lib.enums import TA_JUSTIFY
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.pdfbase.pdfmetrics import stringWidth
from reportlab.pdfgen import canvas
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image
from reportlab.rl_config import defaultPageSize

from .forms import GeepsForm

def sendMail(form):
	sender = getattr(settings, "EMAIL_HOST_USER", None)
	release = form.data.get('release')
	os = form.data.get('os')
	
	message = "Demande d'activation de Matlab" + release + " de " + form.data.get('first_name') + " " + form.data.get('name') + " pour le systeme " + os + "."

	"""Envoi mail à cri@geeps"""
	email = EmailMessage(
		"Activation Licence MatLab",
		message,
		sender,
		# ["cri@geeps.centralesupelec.fr"],
		["diego.daninthe@u-psud.fr"],
		attachments=[generateAttachedCSV(form), generateAttachedPDF(form)],
	)
	
	email.send()
	
	subject = None
	body = None
	
	if form.data.get('language') == 'en':
		subject = "Licence Matlab activation request"
		body = "Your Matlab " + release + " request activation for your " + os + " operating system was well taken into account.\n\nGeePs\'CRI"
	else:
		subject = "Demande d'activation de la licence Matlab"
		body = "Votre demande d'activation de Matlab " + release + " a bien ete prise en compte pour votre systeme " + os + ".\n\nLe CRI du GeePs"
		
	#Acquittement
	#send_mail(subject, body, sender, [form.data.get('email')], fail_silently=False)

"""Return the parameters for an attached csv"""
def generateAttachedCSV(form):
	firstName = form.data.get('first_name')
	name = form.data.get('name')
	email = form.data.get('email')
	phone = form.data.get('phone')
	release = form.data.get('release')
	os = form.data.get('os')
	office = form.data.get('office')
	building = form.data.get('building')
	hostid = form.data.get('hostid')
	
	date = datetime.date.today().strftime('%d-%m-%Y')
	filename = "matlab-" + release + "-" + firstName + "_" + name + "-" + date + ".csv"
	
	activationLabel = firstName + "-" + name + "-" + release + "-" + date
	
	file = StringIO()
	writer = csv.writer(file)
	writer.writerow(['ActivationLabel', 'MatlabRelease', 'HostID', "Name", "Firstname", "Email", "Office", "Phone", "Building", "OperatingSystem"])
	writer.writerow([activationLabel, release, hostid, name, firstName, email, office, phone, building, os])

	return filename, file.getvalue(), "text/csv"

"""Return the parameters for an atached pdf"""
def generateAttachedPDF(form):
	firstName = form.data.get('first_name')
	name = form.data.get('name')
	email = form.data.get('email')
	phone = form.data.get('phone')
	release = form.data.get('release')
	os = form.data.get('os')
	office = form.data.get('office')
	building = form.data.get('building')
	hostid = form.data.get('hostid')
	
	date = datetime.date.today().strftime('%d/%m/%Y')
	filename = "matlab-" + release + "-" + firstName + "_" + name + "-" + date + ".pdf"
	
	story = []
	doc = SimpleDocTemplate(filename, pagesize=letter,
                        rightMargin=72, leftMargin=72,
                        topMargin=72 ,bottomMargin=18)
	
	title = "MatLab Realease Informations"
	
	logo = getattr(settings, "STATIC_URL", None) + "img/logo.jpg"
	im = Image(logo, 2 * inch, 2 * inch)
	story.append(im)
	 
	styles=getSampleStyleSheet()
	styles.add(ParagraphStyle(name='Justify', alignment=TA_JUSTIFY))
	 
	ptext = '<font size=22>%s</font>' % title
	story.append(Paragraph(ptext, styles["Normal"]))       
	story.append(Spacer(1, 24))
	
	ptext = '<font size=14>Demande de licence du %s:</font>' % date
	story.append(Paragraph(ptext, styles["Normal"]))
	story.append(Spacer(1, 12))
	 
	ptext = '<font size=12>Name: %s\n Firstname: %s \nEmail: %s\nPhone: %s\nOffice: %s\nBuilding: %s\nMatlab Release: %s\nOperating System: %s\n HostID: %s</font>' % (firstName, 
																									name,
																									email,
																									phone,
																									office,
																									building,
																									release,
																									os,
																									hostid)
	story.append(Paragraph(ptext, styles["Justify"]))
	story.append(Spacer(1, 12))
	 
	return filename, doc.build(Story), "application/pdf"
	
