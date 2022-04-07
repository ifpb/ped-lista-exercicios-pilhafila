from fila import Fila

class FilaCheiaException(Exception):
    def __init__(self, msg):
        self.msg = msg    

class FilaIngressos(Fila):
    def __init__(self, capacidade=10):
        super().__init__()
        self.__capacidade = capacidade
        self.__count = 0
    
    @property
    def capacidade(self):
        return self.__capacidade

    @capacidade.setter
    def capacidade(self, capacidade):
        self.__capacidade = capacidade

    @property
    def count(self):
        return self.__count

    def add(self, valor):
        if  self.__count >= self.__capacidade:
            raise FilaCheiaException("Fila cheia, tente novamente mais tarde")
        super().add(valor)
        self.__count += 1

    def remove(self):
        super().remove()
        self.__count -= 1
