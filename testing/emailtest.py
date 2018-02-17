import imaplib

username = 'yhong29@jh.edu'
password = 'does3874SIGN'

pop3_ssl_host = 'outlook.office365.com'

popserver = poplib.POP3_SSL(pop3_ssl_host)
popserver.user(username)
popserver.pass_(password)