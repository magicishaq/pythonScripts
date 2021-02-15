#how to check email inbox
import imapclient
yourEmail = 'example@gmail.com'
yourPassword = 'example'



conn = imapclient.IMAPClient('imap.gmail.com', self=True)

conn.login(yourEmail, yourPassword) #returns if true

conn.select_folder('INBOX', readonly=True) #just so we dont delete any emails



UID = conn.search(['SINCE 20-Aug-2020'])

rawMessage = conn.fetch([], ['BODY[]', 'FLAGS'])
specificUID = rawMessage[0]
byteData = b'BODY[]'
import pyzmail
message = pyzmail.PzzMessage.factory(rawMessage[specificUID][byteData])



message.get_subject()
message.get_addresses('from')
