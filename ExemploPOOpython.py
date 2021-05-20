# -*- coding: utf-8 -*-
"""
@author: JESS

Desenvolva uma solução em Python que receba input “1” para “GATO” e “2” para “CACHORRO”.
Quando selecionada a opção “1”, o output deve ser “Miau”. Quando o a opção for “2”, o output deve ser “Auau”. Se o input for “histórico”, o output deve apresentar a lista de execuções do software.
Para sua solução, você deve se atentar para duas obrigatoriedades: conter polimorfismo e Design Pattern Singleton (ou outro de sua preferência).
O exemplo a seguir, ilustra a solução:
Input: 1
Output: Miau
Input: 2
Output: Auau
Input: 2
Output: Auau
Input: histórico
Output: 1 Miau
2 Auau
2 Auau

"""

class Animal():
    _som = ''
    
    def emitirSom(self):
        return self._som
        
class Gato(Animal):
    _som = 'Miau'
    
class Cachorro(Animal):
    _som = 'Auau'
    
def atualizaHistorico(historico):
        historico.append([entrada, som])
        print(som)
    
def imprimeHistorico(historico):
    for linha in historico:
        print(linha[0], linha[1])
    
if __name__ == '__main__':
    
    cat = Gato()
    dog = Cachorro()
    historico = []
    som = ''

    while True:
        entrada = str(input())

        if not entrada!='historico':
            imprimeHistorico(historico)
            break
        elif entrada == '1':
            som = cat.emitirSom()
            atualizaHistorico(historico)
        elif entrada == '2':
            som = dog.emitirSom()
            atualizaHistorico(historico)
                    
            