#!/usr/bin/python

import poplib

username = 'sebastian@winonaesolutions.net'
passwd = '*'
mail_server = 'mail.office365.com'

p = poplib.POP3(mail_server)
p.user(username)
p.pass_(passwd)
for msg_id in p.list()[1]:
	print msg_id
	outf = open('%s.eml' % msg_id, 'w')
	outf.write('\n'.join(p.retr(msg_id)[1]))
	outf.close()
p.quit()