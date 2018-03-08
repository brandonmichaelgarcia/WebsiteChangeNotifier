#!/usr/bin/env python3



######################################################################
class email_message:
    def __init__(self, url):
        sender = "google_user_name@gmail.com"
        recipient = "google_user_name@gmail.com"
        subject = "Website Changed!"
        body_text = "Hello, " + url + " has changed. Go to the website to observe the change."


    def prompt_for_email_message(self):
        while True:
            prompt_for_sender()
            prompt_for_recipient()
            prompt_for_subject()
            prompt_for_body_text()
            print("\nDo you want the following message [y\n]:")
            print_email_message()
            if "n" in (input("\nType 'y' if you are happy with this message or 'n' if you want to edit this message.")).lower():
                break
        return self
        
        
    def prompt_for_sender(self):
        prompt = "Please provide the email address of the sender (presumably you)."
        address = input(prompt)
        while not isValidEmail(address):
            print("Sorry you did not seem to enter a valid email address.")
            address = input(prompt)
        self.sender = address
        
        
    def prompt_for_recipient(self):
        prompt = "If you want to send the nofification of change to someone else, please provide the email address of the receipent.\nOtherwise, hit enter."
        address = input(prompt)
        if address == "":
            self.recipient = self.sender
        else:
            while not isValidEmail(address):
                print("Sorry you did not seem to enter a valid email address.")
                address = input(prompt)
            self.recipient = address
     
     
    def prompt_for_subject(self):
        print("Hit enter, if you would like to use the following subject line:")
        default_subject = "Website Changed!"
        print(default_body_text)
        text = input("Otherwise, enter your custom subject line below and hit enter to submit.")
        self.subject = default_subject if text == "" else text
     
     
    def prompt_for_body_text(self):
        print("Hit enter, if you would like to use the following body text:")
        default_body_text = "Hello, " + self.url + " has changed. Go to the website to observe the change."
        print(default_body_text)
        text = input("Otherwise, enter your custom message below and hit enter to submit.")
        self.body_text = default_body_text if text == "" else text
        
        
    def print_email_message(self):
        print("Sender: {:s}".format(self.sender))
        print("Recipient: {:s}".format(self.recipient))
        print("Subject: {:s}".format(self.subject))
        print("Body Text: {:s}".format(self.body_text))
        
        
    def isValidEmail(address):
        return re.match(r"[^@]+@[^@]+\.[^@]+", address)

    
    def getSender(self): return self.sender
    
    def getRecipient(self): return self.recipient
    
    def getSubject(self): return self.subject
    
    def getBodyText(self): return self.body_text
    
    
    