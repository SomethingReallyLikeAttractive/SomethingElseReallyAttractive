import poplib
import Loader
#vedantchan@gmail.com pop.gmail.com #
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
        inboxStatus = POP3Agent.stat()
        if not inboxStatus[0] == 0
            

    def readEmails(self):



class Mail(FileLoader):
    def __init__(self, fileName):
        fileOpened = open(fileName, "r")
        self.text = fileOpened.read()



