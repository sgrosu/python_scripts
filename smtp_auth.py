#!/home/sgrosu/anaconda2/bin/python

import smtplib
import email

mail_server = 'email.ethicalcomms.co.uk'
mail_server_port = 25
from_address = 'sebastian@centdesk.learn'
to_address = 'sebastian@winonaesolutions.net'

from_header = 'From %s\r\n' % from_address
to_header = 'To %s\r\n' % to_address
subject_header = 'Subject: something interesting'

body = 'This is a test email testing smtp authentication'

email_message = '%s\n%s\n%s\n\n%s' % (from_header,to_header,subject_header,body)

try:
	s = smtplib.SMTP(mail_server)
	s.set_debuglevel(1)
	#s.starttls()
	s.login('emailerbounce@ethicalcomms.co.uk','P@ssw0rd')
	s.sendmail(from_address,to_address,email_message)
	log.info("Successfully sent email")
except smtplib.SMTPException:
	log.info("Error: Unable to send email")
#finally:
#    s.quit()