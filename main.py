from ClasesMMU import *

def mmu(paginas,frames,archivo):
    lista_paginas=[]
    cola=initq(frames)
    ordenpaginas=Cola()
    for i in range(paginas):
        lista_paginas.append(page(i))


    with open(archivo) as f:
        for line in f:
            operacion= line[0]
            pagina= int(line[1])

            if operacion== "R":
                if verificarcarga(lista_paginas,pagina):
                    lista_paginas[pagina].modifybit(operacion)
                else:

