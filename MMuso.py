class page:
    def __init__(self,frame):
        self.bit= [1,0,0]
        self.frame= frame

    def modifyframe(self,frame):
        self.frame= None

    def modifybit(self,task):
        if task== "R": 
            self.bit[1]=1
        
        elif task== "W":
            self.bit[1]=1
            self.bit[2]=1

        elif task== "F":
            self.bit[0]=0

    def getframe(self):
        return self.frame
    
    def getbit(self):
        return self.bit
    
class Cola:
    def __init__(self):
        self.q=[]
    def enq(self,x):
        self.q.insert(0,x)
    def deq(self):
        assert len(self.q)>0
        return self.q.pop()
    def is_empty(self):
        return len(self.q)==0
    def size(self):
        return len(self.q)
    def getq(self):
        return self.q


