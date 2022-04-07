from no import No

class PilhaVaziaException(Exception):
    def __init__(self, msg):
        self.msg = msg

class Pilha:
    def __init__(self):
        self.__topo = None
    
    @property
    def topo(self):
        return self.__topo

    @topo.setter
    def topo(self, topo):
        self.__topo = topo

    def push(self, valor):
        novo = No(valor)
        if self.__topo is None:
            self.__topo = novo
            return

        novo.prox = self.__topo
        self.__topo = novo

    def pop(self):
        if self.__topo is None:
            raise PilhaVaziaException("Pilha vazia, não é possível remover")
        elemento = self.__topo
        self.__topo = self.__topo.prox
        return elemento

    def remover_ate_elemento(self, elemento):
        atual = self.topo

        ## varre os elementos anteriores ao que se deseja encontrar
        while atual is not None and atual.carga is not elemento:
            if atual.prox is not None:
                self.topo = atual.prox
            atual = atual.prox

        ## remove o próprio elemento quando encontrado
        if atual is not None and atual.carga == elemento:
            self.topo = atual.prox
        ## esvazia a lista quando nenhum elemento foi encontrado
        else:
            self.topo = None

    def is_empty(self):
        return self.__topo is None

    def __str__(self):
        return "[%s]" % self.__topo
