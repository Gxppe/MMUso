from ClasesMMU import *

def mmu(paginas,frames,archivo):
    lista_paginas=[]
    cola=initq(frames)
    ordenpaginas=Cola()
    for i in range(paginas):
        lista_paginas.append(page(i))
    with open(archivo) as f:
        contador=0
        for line in f:

            operacion= line[0]
            pagina= int(line[1])
            print("Operacion:",line)
            print("inicio",cola)
            
            if verificarcarga(lista_paginas,pagina):
                lista_paginas[pagina].modifybit(operacion)
                print("entre if",contador)
            else:
                cargarpagina(lista_paginas,pagina,cola,ordenpaginas)
                lista_paginas[pagina].modifybit(operacion)
                print("entre else",contador)
                contador+=1
            print()
            for i in range(paginas):
                print("Pagina: ",lista_paginas[i].getpage()," Bit: ",lista_paginas[i].getbit()," Frame: ",lista_paginas[i].getframe())
            print("final",cola)

