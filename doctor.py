import random
from breezypythongui import EasyFrame

class View (EasyFrame):

    def __init__(self, d):

        EasyFrame.__init__(self)
        self.doctor = d
        self.doctorLabel = self.addLabel(text = "Doctor",
                                         sticky = "W", row = 0, column = 0)
        self.doctorField = self.addTextField(text = self.doctor.greeting(),
                                             row = 0, column = 1, width = 100,
                                             columnspan = 2, state = "disabled")

        self.patientLabel = self.addLabel(text = "User", sticky = "W",
                                          row = 1, column = 0)
        self.patientField = self.addTextField(text = "", sticky = "NSEW",
                                              row = 1, column = 1, columnspan = 2)

        self.respondButton = self.addButton(text = "Send Response", row = 2,
                                            column = 0, command = self.respond)

        self.leaveButton = self.addButton(text = "Leave Conversation", row = 2,
                                          column = 1, command = self.leave)
        self.newButton = self.addButton(text = "New Conversation", row = 2,
                                        column = 2, command = self.new)

    def respond(self):
        self.doctorField.setText(self.doctor.reply(self.patientField.getText()))

    def leave(self):
        self.doctorField.setText(self.doctor.signoff())
        self.patientField.setText("")

    def new(self):
        self.doctorField.setText(self.doctor.greeting())
        self.patientField.setText("")

class Doctor():
    def __init__(self):
        self.hedges = ("Please tell me more.",
                       "Many of my patients tell me the same thing.",
                       "Please continue.")

        self.qualifiers = ("Why do you say that? ",
                           "You seem to think that ",
                           "Can you explain why?")

        self.replacements = {"I": "You", "me":"you", "my":"you",
                             "we":"you", "us":"you", "mine":"yours"}

    def greeting(self):
        return "Good morning, I hope you are well today. What I can do for you?"

    def signoff(self):
        return "Thank you for consulting me. Have a nice day!"

    def reply(self, sentence):
        probability = random.randint(1, 4)
        if probability == 1:
            return random.choice(self.hedges)
        else:
            return random.choice(self.qualifiers) + self.changePerson(sentence)

    def changePerson(self, sentence):
        words = sentence.split()
        replyWords = []
        for word in words:
            replyWords.append(self.replacements.get(word, word))
        return " ".join(replyWords)
