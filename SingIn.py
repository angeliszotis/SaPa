import time
class SingIn():
    frase="123"

    def __init__(self,frase):
        
        if self.frase != frase:
            self.wrongFrase()
        else:
            self.correctFrace()
    def wrongFrase(self):
        return "Fail" 
    def correctFrace(self):
        return "Correct Frace"
