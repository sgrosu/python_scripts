#!/usr/bin/python
'''
connect to my gmail inbox and fetch all the mails and display their subject and from address

'''

import imaplib
obj = imaplib.IMAP4_SSL('imap.gmail.com',993)
obj.login('dumblinuxuser','secretpass')

status, msgs = obj.select()

if status == 'OK':
	obj.select('INBOX')  # <-- response like ('OK', ['74']) --> total no. of mail in sent folder 
	#mboxes = obj.list()
	#print mboxes
	result, data = obj.search(None, "ALL")
	ids = data[0] # data is a list.
	id_list = ids.split() # ids is a space separated string
	latest_email_id = id_list[-1] # get the latest
	 
	#result, data = obj.fetch(latest_email_id, "(RFC822)") # fetch the email body (RFC822) for the given ID
 	#raw_email = data[0][1] # here's the body, which is raw text of the whole email
 	#print raw_email

 	for emaill in id_list:
 		result, data = obj.fetch(emaill, '(BODY[HEADER.FIELDS (SUBJECT FROM)])')
 		header_data = data[0][1]
 		print header_data 

# including headers and alternate payloads
else:
	print status
 	print msgs




