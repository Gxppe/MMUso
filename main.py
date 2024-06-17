from ClasesMMU import *

def mmu(paginas,frames,archivo):
    lista_paginas=initpages(paginas)
    cola=initq(frames)
    with open(archivo) as f:
        for line in f:
            operacion= line[0]
            pagina= int(line[1])

            if lista_paginas[pagina].getframe()==None:
                if cola.size()>0:
                    frame= cola.deq()
                    lista_paginas[pagina].loadpage(frame)
                else:
                    print("No hay frames disponibles")


mmu(10,3,"ejemplo")