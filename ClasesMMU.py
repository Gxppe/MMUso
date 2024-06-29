class page:
    def __init__(self,page,frame=-1):

#bit[0]: V
#bit[1]: U
#bit[2]: D

        self.page= page     
        self.bit= [0,0,0]
        self.frame= frame

    def modifyframe(self,frame):
        self.frame= frame

    def modifybit(self,task):
        if task== "R": 
            self.bit[1]=1
        elif task== "W":
            self.bit[1]=1
            self.bit[2]=1
        elif task== "F":
            self.bit[0]=0 
            self.modifyframe(-1)

    def loadpage(self,frame):
        self.frame= frame
        self.bit[0]=1
        self.bit[1]=0
        self.bit[2]=0


    def getframe(self):
        return self.frame
    
    def getbit(self):
        return self.bit
    
    def getpage(self):
        return self.page
    
    
class Cola:
    def __init__(self):
        self.q=[]

    def enq(self,x):
        self.q.insert(0,x)

    def deq(self):
        assert len(self.q)>0
        return self.q.pop()
    
    def is_empty(self):
        return len(self)==0
    
    def size(self):
        return len(self.q)
    
    def getq(self):
        return self.q
    
    def __str__(self):
        return f"Cola: {self.q}"


def initq(rango):
    cola=Cola()
    for i in range(rango):	
        cola.enq(i)
    return cola

def initpages(rango):
    pages=[]
    for i in range(rango):
        pages.append(page(i))
    return pages

def verificarcarga(lista_paginas,pagina):
    if lista_paginas[pagina].getbit()[0]==1:
        return True
    return False

def cargarpagina(lista_paginas,pagina,colaframes,colapaginas):
    if colaframes.size()==0:
        paginavictima=colapaginas.deq()
        lista_paginas[pagina].loadpage(paginavictima.getframe())
        lista_paginas[paginavictima.getpage()].modifybit("F")
        colapaginas.enq(lista_paginas[pagina])
    else:
        frame=colaframes.deq()
        lista_paginas[pagina].loadpage(frame)
        colapaginas.enq(lista_paginas[pagina])