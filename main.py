from fila import Fila
from fila_ingressos import FilaCheiaException, FilaIngressos
from pilha import Pilha
from pilha_palindromo import PilhaPalindromo

"""
Q1
"""
pilha = Pilha()
pilha.push(44)
pilha.push(65)
pilha.push(32)
pilha.push(54)
print(pilha)

"""
Q2
"""
pilha.remover_ate_elemento(34)
print(pilha)

"""
Q3
"""
if PilhaPalindromo.checa_palindromo("socorram me subi no onibus em marrocos"):
  print("Palíndromo!")
else:
  print("Não é palíndromo!")

"""
Q4
"""
print("Fila")
fila = Fila()
fila.add(321)
fila.add(542)
fila.add(853)
fila.add(124)
print(fila)
print(fila.remove())
print(fila)

"""
Q5
"""
print("Fila ingressos")
fila_ingressos = FilaIngressos(3)
try:
    fila_ingressos.add("diego@teste.com")
    fila_ingressos.add("diego2@teste.com")
    fila_ingressos.add("diego3@teste.com")
    fila_ingressos.add("diego5@teste.com")
except FilaCheiaException as f:
    print(f.msg)

fila_ingressos = FilaIngressos(12)
try:
    fila_ingressos.add("diego@teste.com")
    fila_ingressos.add("diego2@teste.com")
    fila_ingressos.add("diego3@teste.com")
    fila_ingressos.add("diego4@teste.com")
    fila_ingressos.add("diego5@teste.com")
    fila_ingressos.remove()
    print(fila_ingressos)
except FilaCheiaException as f:
    print(f.msg)