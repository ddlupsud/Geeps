import os as os_module
import csv
import datetime

from django.conf import settings
from django.core.mail import send_mail, EmailMessage

from io import BytesIO, StringIO

from reportlab.lib.units import inch
from reportlab.lib.enums import TA_CENTER
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.pdfgen import canvas
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image
from reportlab.rl_config import defaultPageSize

from .forms import GeepsForm

"""Send emails with attachments (csv and pdf)"""
def sendMail(form):
	sender = getattr(settings, "EMAIL_HOST_USER", None)
	release = form.data.get('release')
	os = form.data.get('os')
	
	message = "Demande d'activation de Matlab" + release + " de " + form.data.get('first_name') + " " + form.data.get('name') + " pour le systeme " + os + "."
	
	# Envoi mail à cri@geeps
	email = EmailMessage(
		"Activation Licence MatLab",
		message,
		sender,
		["cri@geeps.centralesupelec.fr"],
		attachments=[generateAttachedCSV(form)],
	)
	
	filename, pdf, mimetype = generateAttachedPDF(form)
	email.attach(filename, pdf, mimetype)
	email.send()
	
	subject = None
	body = None
	
	if form.data.get('language') == 'en':
		subject = "Licence Matlab activation request"
		body = "Your Matlab " + release + " request activation for your " + os + " operating system was well taken into account.\n\nGeePs\'CRI"
	else:
		subject = "Demande d'activation de la licence Matlab"
		body = "Votre demande d'activation de Matlab " + release + " a bien ete prise en compte pour votre systeme " + os + ".\n\nLe CRI du GeePs"
		
	# Acquittement
	send_mail(subject, body, sender, [form.data.get('email')], fail_silently=False)

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
	
	date = datetime.date.today().strftime('%Y-%m-%d')
	filename = "matlab-" + release + "-" + firstName + "_" + name + "-" + date + ".csv"
	
	activationLabel = firstName + "-" + name + "-" + release + "-" + date
	
	file = StringIO()
	writer = csv.writer(file)
	writer.writerow(['ActivationLabel', 'MatlabRelease', 'HostID', "Name", "Firstname", "Email", "Office", "Phone", "Building", "OperatingSystem"])
	writer.writerow([activationLabel, release, hostid, name, firstName, email, office, phone, building, os])
	
	csvFile = file.getvalue()
	file.close()
	
	return filename, csvFile, "text/csv"

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
	
	date = datetime.date.today()
	filename = "matlab-" + release + "-" + firstName + "_" + name + "-" + date.strftime('%Y-%m-%d') + ".pdf"
	title = "MatLab Realease Informations"
	
	buffer = BytesIO()
	
	story = []
	doc = SimpleDocTemplate(buffer, pagesize=letter,
                        rightMargin=72, leftMargin=72,
                        topMargin=72, bottomMargin=18)
		
	logo = os_module.path.join(os_module.path.dirname(os_module.path.abspath(__file__)), "static", "img", "logo.jpg")
	im = Image(logo, 2 * inch, 2 * inch)
	story.append(im)
	
	styles = getSampleStyleSheet()
	styles.add(ParagraphStyle(name='Center', alignment=TA_CENTER))
	 
	ptext = '<font size=22>%s</font>' % title
	story.append(Paragraph(ptext, styles["Center"]))       
	story.append(Spacer(1, 36))
	
	ptext = '<font size=14>Demande de licence du %s</font>' % date.strftime('%d/%m/%Y')
	story.append(Paragraph(ptext, styles["Normal"]))
	story.append(Spacer(1, 24))
	
	ptext = '<font size=12>Name: %s</font>' % name
	story.append(Paragraph(ptext, styles["Normal"]))
	story.append(Spacer(1, 12))
	
	ptext = '<font size=12>Firstname: %s</font>' % firstName
	story.append(Paragraph(ptext, styles["Normal"]))
	story.append(Spacer(1, 12))
	
	ptext = '<font size=12>Email: %s</font>' % email
	story.append(Paragraph(ptext, styles["Normal"]))
	story.append(Spacer(1, 12))
	
	ptext = '<font size=12>Phone: %s</font>' % phone
	story.append(Paragraph(ptext, styles["Normal"]))
	story.append(Spacer(1, 12))
	
	ptext = '<font size=12>Office: %s</font>' % office
	story.append(Paragraph(ptext, styles["Normal"]))
	story.append(Spacer(1, 12))
	
	ptext = '<font size=12>Building: %s</font>' % building
	story.append(Paragraph(ptext, styles["Normal"]))
	story.append(Spacer(1, 12))
	
	ptext = '<font size=12>Matlab Realease: %s</font>' % release
	story.append(Paragraph(ptext, styles["Normal"]))
	story.append(Spacer(1, 12))
	
	ptext = '<font size=12>Operating System: %s</font>' % os
	story.append(Paragraph(ptext, styles["Normal"]))
	story.append(Spacer(1, 12))
	
	ptext = '<font size=12>HostID: %s</font>' % hostid
	story.append(Paragraph(ptext, styles["Normal"]))
	story.append(Spacer(1, 12))
	
	doc.build(story)
	pdf = buffer.getvalue()
	buffer.close()
	
	return filename, pdf, "application/pdf"
