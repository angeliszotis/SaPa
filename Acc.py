class Acc(object):
    def __init__(self,acc,username,password):
        self.acc=acc
        self.username=username
        self.password=password

    def toString(self):
        return '{}\n Username:{}\n Password:{}'.format(self.acc,self.username,self.password)

p1 = Acc('test','test','test')
print p1.toString()
