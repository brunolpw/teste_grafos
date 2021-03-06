#!/usr/bin/env python
# -*- coding: utf-8 -*-

from random   import randint
from operator import attrgetter

from sugestao import Sugestao
from turma    import Turma
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
    
    """
        Aqui a pontuação de cada elemento deve ser ajustada para a turma
    selecionada, levando em consideração os tópicos anteriores e possiveis
    sugestões futuras.
        ->  Sugestões que possuem dependencias (outros temas previos), que
    não foram abordados, devem sofrer um decremento de 5 pontos, ou ser
    igual a 0 (zero).
        ->  Sugestões que possuem dependencias já abordadas, terão sua
    pontuação acrescida em 5 pontos, o intuito aqui é dar continuidade ao
    estudo.
        ->  Sugestões que tiverem um orçamento acima da média terão seus
    pontos decrementados em 3.
        ->  Sugestões que tiverem um orçamento abaixo da média terão seus
    pontos acrescidos em 3.
    """
    def ajusta_pontuacao(self):
        new_sugs = []
        valores  = []
        media    = 0
        turma = Turma() # pegar histórico de anos e matérias da turma.
        for t in self.b.read_sugestoes_from_turmas():
            valores.append(self.b.read_valor_itens_sugestao(t))
        media = sum(valores)//len(valores)
        for sug in self.sugs:
            # aplicar as regras
            itens = self.b.read_itens_from_sugestoes(sug)
            dependencias = self.b.read_path(sug)
            sug.add_itens(itens)
            sug.add_dependencias(dependencias)
            new_sugs.append(sug)
        return new_sugs

    def verifica_itens(self):
        pass
    """
        A roleta deve pegar todos os pontos de todos os elementos do banco
    de dados, já tratados para a devida turma, tendo a sua pontuação já
    ajustada para este momento, logo ela irá organizar cada valor dentro
    de uma "roleta viciada", onde selecionará o elemento, para isso ela
    levará em consideração a pontuação, dando mais chance aqueles
    individuos que tiverem a melhor, mas não excluido por completo os
    mais "fracos".
    """
    def roleta(self):
        total   = self.b.read_sum_pontos_from_sugestoes()
        sorteio = randint(0, total)
        posicao = -1
        while sorteio > 0:
            posicao = posicao + 1
            sorteio = sorteio - self.sugs[posicao].pontos

        itens = self.b.read_itens_from_sugestoes(self.sugs[posicao])
        dependencias = self.b.read_path(self.sugs[posicao])
        self.sugs[posicao].add_itens(itens)
        self.sugs[posicao].add_dependencias(dependencias)
        return self.sugs[posicao].to_string()

