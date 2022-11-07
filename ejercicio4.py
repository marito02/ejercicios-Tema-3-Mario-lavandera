#Implementar sobre el TDA polinomio desarrollado previamente las siguientes actividades:
#• restar dos polinomios;
#• dividir el polinomio por un numero;
#• eliminar un término;
#• determinar si un término existe en un polinomio

class Polinomio():
    def __init__(self):
        self.termino_mayor = None
        self.grado = 1
    def crear_termino(polinomio, valor, termino):
        polinomio.termino_mayor = None
        aux.informacion = datoPolinomio(valor, termino)
        if (termino > polinomio.grado):
            aux.siguiente=polinomio.termino_mayor
            polinomio.termino_mayor=aux
            polinomio.grado=termino
        else:
            actual=aux 
            while(actual.siguiente is not None and termino < actual.siguiente.informacion.termino):
                actual=actual.siguiente 
                aux.siguiente=actual.siguiente
                actual.siguiente=aux
    def obtener_valor(polinomio, termino):
        aux=polinomio.termino_mayor
        while (aux is not None and aux.informacion.termino > termino):
            aux=aux.siguiente
        if(aux is not None and aux.informacion.termino == termino):
            return aux.informacion.valor
        else:
            return O
    def mostrar(polinomio):
        aux=polinomio.termino_mayor
        pol=" "
        if (aux is not None):
            while (aux is not None):
                signo=" "
                if (aux.informacion.valor >= 0):
                    pol += signo + str(aux.informacion.valor) + "x^2" + str(aux.informacion.termino)
    def restar(polinomio1,polinomio2):         
        polinomio1=Polinomio(6,3)
        polinomio2=Polinomio(4,2)
        polinomio_aux=Polinomio()
        mayor=polinomio1 if (polinomio1.grado > polinomio2.grado) else polinomio2
        for i in range(0,mayor.grado+1):
            resta = obtener_valor(polinomio1,i) - obtener_valor(polinomio2,i)
            if(resta != 0):
                crear_termino(polinomio_aux,i,resta)
                return polinomio_aux
    def dividir(polinomio1,polinomio2):
        mayor=polinomio1 if (polinomio1.grado > polinomio2.grado) else polinomio2
        for i in range(0,mayor.grado+1):
            division=obtener
    def eliminar_termino(polinomio,valor,grado):
        grado=polinomio.grado
        valor=polinomio.valor
        eliminar=int(input("Introduzca el numero que quiere que se elimine: "))
        if (eliminar==grado):
            polinomio.grado=0
            return str(polinomio.valor) + "x^2" + str(polinomio.grado)
    def buscar(polinomio):
        aux=Nodo()
        aux.informacion=polinomio
        grado=polinomio.grado
        valor=polinomio.valor
        for polinomio in Polinomio:
            buscar=input(f"Introduzca el polinomio para buscar:str{polinomio.valor} + x^2 + str{polinomio.grado}")
            polinomio=buscar
            polinomo_buscar=polinomio.crear_termino
            if polinomio_buscar in Polinomio:
                print(f"El polinomio {polinomio.buscar} ha sido encontrado")
            else:
                print(f"No se ha hallado ningun polinomio {polinomio.buscar}")

            






            




        
