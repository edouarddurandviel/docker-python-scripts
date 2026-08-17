class SubmitForm:
    addrNbr = 464

    def __init__(self, firstname, lastname="Durand"):
        self.firstname = firstname
        self.lastname = lastname

    def getFullName(self):
        return f"{self.firstname} {self.lastname}"

    def getAddr(self):
        return f"{self.firstname} {self.lastname}: {self.addrNbr} chemin du petit four"