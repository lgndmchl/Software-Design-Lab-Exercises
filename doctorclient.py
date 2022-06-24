from breezypythongui import EasyFrame
from codecs import decode
from socket import *
import os
import pickle
from threading import Thread
from doctorclienthandler import DoctorClientHandling

HOST = "127.0.0.1"
PORT = 6942
CODE = "ascii"
BUFSIZE = 1001
ADDRESS = (HOST, PORT)

class DoctorClient(EasyFrame):

    COLOR = "#CCEEFF"
    def __init__(self):
        EasyFrame.__init__(self, title="Doctor", background=DoctorClient.COLOR)
        self.nameLabel = self.addLabel(text="Name?", row=0, column=0, background=DoctorClient.COLOR)
        self.nameField = self.addTextField(text="", row=0, column=1, width=15)
        self.drLabel = self.addLabel(text="Want to connect?", row=1, column=0, columnspan=2, background=DoctorClient.COLOR)
        self.ptField = self.addTextField(text="", row = 2, column = 0, columnspan = 2,width = 50)
        self.sendBtn = self.addButton(row=3, column=0, text="Send reply", command=self.sendReply, state="disabled")
        self.connectBtn = self.addButton(row=3, column=1, text="Connect", command=self.connect)
        self.ptField.bind("<Return>", lambda event: self.sendReply())

    def connect(self):
        self.server = socket(AF_INET, SOCK_STREAM)
        self.server.connect(ADDRESS)
        self.server.send(bytes(self.nameField.getText(), CODE))
        self.drLabel["text"] = decode(self.server.recv(BUFSIZE), CODE)
        self.connectBtn["text"] = "Disconnect"
        self.connectBtn["command"] = self.disconnect
        self.sendBtn["state"] = "normal"
        self.ptField.setText("")

    def sendReply(self):
        """Sends patient input to doctor, receives
        and outputs the doctor's reply."""
        ptInput = self.ptField.getText()
        if ptInput != "":
            self.server.send(bytes(ptInput, CODE))
            drReply = decode(self.server.recv(BUFSIZE),CODE)
            if not drReply:
                self.messageBox(message = "Doctor disconnected")
                self.disconnect()
            else:
                self.drLabel["text"] = drReply
                self.ptField.setText("")

    def disconnect(self):
        self.server.close()
        self.ptField.setText("")
        self.drLabel["text"] = ""
        self.connectBtn["text"] = "Connect"
        self.connectBtn["command"] = self.connect
        self.sendBtn["state"] = "disabled"


class DoctorClientHandler(Thread):
    def __init__(self, client):
        Thread.__init__(self)
        self.client = client
        self.dr = None
        self.patientName = None

    def run(self):
        self.patientName = decode(self.client.recv(BUFSIZE), CODE)

        if os.path.exists(self.patientName + ".dat"):
            file = open(self.patientName + ".dat", "rb")
            self.dr = pickle.load(file)
        else:
            self.dr = DoctorClientHandling(Thread)
        self.client.send(bytes(self.dr.greeting(), CODE))
        while True:
            message = decode(self.client.recv(BUFSIZE), CODE)
            self.dr.history.append(message)
            if not message:
                file = open(self.patientName + ".dat", "wb + ")
                pickle.dump(self.dr, file)
                print("Client disconnected")
                self.client.close()
                break
            else:
                self.client.send(bytes(self.dr.reply(message), CODE))


def main():
    DoctorClient().mainloop()

if __name__ == "__main__":
    main()


