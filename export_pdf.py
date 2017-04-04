#!/home/sgrosu/anaconda2/bin/python

import subprocess
import datetime
from reportlab.pdfgen import canvas
from reportlab.lib.units import cm

def disk_report():
	p = subprocess.Popen("df -h",shell=True,stdout=subprocess.PIPE)
	return p.stdout.readlines()

def create_pdf(input,output='/home/sgrosu/python/disk_report.pdf'):
	now = datetime.datetime.today()
	date = now.strftime("%h %d %Y %H:%M:%S")
	c = canvas.Canvas(output)
	#c.setFont("Courier",10)
	#c.drawString(100,500,"Hello World")
	textobject = c.beginText()
	textobject.setTextOrigin(cm,20*cm)
	textobject.textLines('''
			Disk capacity Report: %s
			''' % date
		)
	#c.drawString(0,100,"Disk capacity Report: %s" % date)
	#i = 250
	for line in input:
		textobject.textLine(line.strip())
	c.drawText(textobject)
	c.showPage()
	c.save()
	#print c

report = disk_report()
#print report
create_pdf(report)