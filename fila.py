from no import No


class FilaVaziaException(Exception):
    def __init__(self, msg):
        self.msg = msg

class Fila:
    def __init__(self):
        self.__inicio = None
        self.__fim = None

    def add(self, valor):
        novo = No(valor)
        if self.__inicio is None or self.__fim is None:
            self.__inicio = self.__fim = novo
        else:
            novo.prox = self.__fim
            self.__fim = novo

    def remove(self):
        if self.__inicio is None:
            raise FilaVaziaException("Fila vazia, não é possível remover")
        atual = self.__fim
        while atual.prox is not self.__inicio:
            atual = atual.prox
        elemento = atual.prox
        self.__inicio = atual
        self.__inicio.prox = None
        return elemento

    def __str__(self):
        return "[%s]" % (self.__fim)

    def is_empty(self):
        return self.__inicio is None and self.__fim is None

