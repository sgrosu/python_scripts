#!/home/sgrosu/anaconda2/bin/python

import smtplib
import email

mail_server = 'localhost'
mail_server_port = 25
from_address = 'sebastian@centdesk.learn'
to_address = 'sgrosu'

from_header = 'From %s\r\n' % from_address
to_header = 'To %s\r\n' % to_address
subject_header = 'Subject: something interesting'

body = 'This is a test email'

email_message = '%s\n%s\n%s\n\n%s' % (from_header,to_header,subject_header,body)

s = smtplib.SMTP(mail_server,mail_server_port)
s.sendmail(from_address,to_address,email_message)
s.quit()