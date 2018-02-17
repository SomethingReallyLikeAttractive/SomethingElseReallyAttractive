import poplib

class Email:
    POP3Agent = None
    emailAddress = ""
    POP3Address = ""
    emailPassword = ""

    def __init__(self, addressInput, POP3Input, passwordInput):
        POP3Agent = poplib.POP3('')

        emailAddress = addressInput
        POP3Address = POP3Input
        emailPassword = passwordInput

    

