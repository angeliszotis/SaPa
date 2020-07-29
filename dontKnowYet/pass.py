class Pass:
    def __init__(self,whereuse,username,password):
       
        self.whereuse = whereuse
        self.username = username
        self.password = password

    def show(self):
        return '{}\nUsername:{}\nPassword:{}'.format(self.whereuse,self.username,self.password)



def test(code):
    
     if code != 123:
            print 'Wrong password'
            exit()
test(1123)

p1 = Pass('tekis','lakis','jonis')
print p1.show()


