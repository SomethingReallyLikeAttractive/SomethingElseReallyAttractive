import imaplib
import time

host = "outlook.office365.com"
port = 993

username = "yhong29@jh.edu"
password = "does3874SIGN"

mail = imaplib.IMAP4_SSL(host, port)
mail.login(username, password)
mail.select("inbox")


