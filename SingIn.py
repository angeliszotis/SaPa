class SingIn:

    frase=123

    def __init__(self,frase):
       
        if self.frase != frase: 
            print 'wrong phrace!'
            exit()

x = input()
p1= SingIn(x)

