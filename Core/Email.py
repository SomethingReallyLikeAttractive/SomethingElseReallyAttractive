import poplib
import Loader

class Email:
    POP3Agent = None
    emailAddress = ""
    emailPassword = ""

    def __init__(self, addressInput, POP3Input, passwordInput):
        POP3Agent = poplib.POP3(POP3Input)
        emailAddress = addressInput
        emailPassword = passwordInput

        POP3Agent.user(emailAddress)
        POP3Agent.pass_(emailPassword)

    def RetrieveNewEmails(self):


class Mail(File):




