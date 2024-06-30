from ClasesMMU import *

def mmu(paginas,frames,archivo):
    lista_paginas=[]
    cola=initq(frames)
    ordenpaginas=Cola()
    for i in range(paginas):
        lista_paginas.append(page(i))
    
    pagefaults=0
    with open(archivo) as f:
        for line in f:
            operacion= line[0]
            pagina= int(line[1])
            if verificarcarga(lista_paginas,pagina):
                if operacion=="F":
                    cola.enq(lista_paginas[pagina].modifybit(operacion))
                else:
                    lista_paginas[pagina].modifybit(operacion)
            else:
                pagefaults+=1
                cargarpagina(lista_paginas,pagina,cola,ordenpaginas)

                if operacion=="F":
                    cola.enq(lista_paginas[pagina].modifybit(operacion))
                else:
                    lista_paginas[pagina].modifybit(operacion)
    generarformato(lista_paginas,paginas,frames,pagefaults,archivo)
            
mmu(6,6,"ejemplo")