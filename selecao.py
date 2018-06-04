#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random
from operator import attrgetter

from sugestao import Sugestao
from banco    import Banco

"""
    A classe de seleção irá pegar todos os valores obtidos no banco de dados
em ordem de pontuação do maior para o menor logo que ela é instanciada, ela
tem como função embaralhar os dados e sortear parte da população de sugestões,
dentro deste novo grupo selecionado aleatóreamente, os individuos serão
classificados pela sua pontuação e ranqueados, os melhores selecionados serão
passados adiante enquanto os menos qualificados serão desclassificados, aqui
será levado em conta requisitos como a necessidade de dependencias e se estas
dependencias já foram vistas anteriormente.
"""
class Selecao(object):
    def __init__(self):
        self.b = Banco()
        self.sugs = self.b.read_all_order_by_pontos()
        self.new_sugs = []
    
    def embaralha(self):
        random.shuffle(self.sugs)
    
    """
        Pega os <quantidade> primeiros valores.
        Indicado que seja algo entre 3 a 7 itens.
    """
    def seleciona(self, quantidade=5):
        self.embaralha()
        embaralhado = self.sugs
        for i in range(quantidade):
            self.new_sugs.append(embaralhado[i])
        self.new_sugs = sorted(self.new_sugs, key=attrgetter('pontos'), reverse=True)


    """
        Aqui será pego o melhor item dentre os selecionados, será verificado
    se há a necessidade de dependencias, se houver será listado quais são elas
    e se pode continuar com o processo ou não, caso não seja possivel, então
    será feita uma nova listagem.
    """
    def pega_melhor(self):
        sug = self.new_sugs[0]
        dependencias = self.b.verifica_dependencias(sug)
        if dependencias > 0:
            sug.remove_pontos(dependencias)
            sug.add_dependencias(self.b.read_path(sug))
            return sug.to_string()
        return ("não tem dependencias. pontos: " + str(sug.pontos))

