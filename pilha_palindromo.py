from pilha import Pilha


class PilhaPalindromo(Pilha):

    def inverter(self):
        """Insere numa pilha auxiliar, o que irá colocar na ordem inversa
        """
        pilha_aux = Pilha()
        atual = self.topo
        while atual is not None:
            pilha_aux.push(atual.carga)
            atual = atual.prox
        return pilha_aux

    def inserir_palavra(self, palavra):
        """ Converte palavra para lista e insere cada caractere como um nó da pilha
            para evitar que a palavra seja inserida na ordem inversa, foi necessário usar uma pilha auxiliar
        """
        pilha_aux = Pilha()

        for letra in list(palavra):
            pilha_aux.push(letra)

        while pilha_aux.topo is not None:
            self.push(pilha_aux.pop().carga)

    def __eq__(self, pilha):
        """ Método que é usado quando se compara uma pilha com outra (pilha == pilha2)
        """
        atual = self.topo
        atual2 = pilha.topo
        while atual is not None and atual2 is not None:
        # Caso algum dos elementos da pilha for diferente, será retornado False
            if atual.carga != atual2.carga:
                return False
            atual = atual.prox
            atual2 = atual2.prox
        return True
            
    @staticmethod
    def checa_palindromo(palavra):
        pilha = PilhaPalindromo()
        pilha.inserir_palavra(palavra.casefold().replace(" ", "")) # Remover espaços e uppercase
        # Palavra vazia é palíndromo
        if pilha.topo == None:
            return True
        # Será palíndromo se a pilha for igual à sua versão inversa
        return pilha == pilha.inverter()