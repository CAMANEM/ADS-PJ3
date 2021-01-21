class lista:
    def __init__(self, sig = None, val = None, ind = None):
        self.nodo = self
        self.primero = None
        self.siguiente = sig
        self.valor = val
        self.indice = ind
        self.contador = 0

    def Add(self, valor):
        if self.primero == None:
            self.primero = lista(val = valor, ind = self.contador)
        
        else:
            ult = self.BuscarUltimo(self.primero)
            ult.siguiente = lista(val = valor, ind = self.contador)

        print ("elemento añadido con el índice", self.contador)
        self.contador += 1



    def BuscarUltimo(self, buscar):
        if buscar.siguiente == None:
            return buscar

        else:
            return self.BuscarUltimo(buscar.siguiente)

    def Obtener(self, i):

        if i > self.contador or 0 > i:
            print ("El índice supera el largo de la lista.")
            return

        else:
            return self.obtener(self.primero, i)

    def obtener(self, elemento, i):
        if elemento.indice == i:
            return elemento.valor
        
        else:
            return self.obtener(elemento.siguiente, i)

    def Largo(self):
        return self.contador