#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    Sugestão é uma classe basica para representar as opções que serão lançadas
pelos professores e que o sistema usará para sugerir de tema para uso em sala
de aula.
"""
class Sugestao(object):
    def __init__(self, id=0, texto='', autor='', itens=[], pontos=0):
        self.id     = id
        self.texto  = texto
        self.autor  = autor
        self.itens  = itens
        self.pontos = pontos
        self.dependencias = []

    def add_ponto(self, ponto=0):
        self.pontos = self.pontos + ponto
        if self.dependencias != None:
            self.pontos = self.pontos - len(self.dependencias)

    def remove_pontos(self, pontos=0):
        self.pontos = self.pontos - pontos
        if self.pontos <= 0:
            self.pontos = 0

    def add_item(self, item=[]):
        self.itens.append(item)

    def add_referencias(self, ref=[]):
        self.dependencias.append(ref)

    def to_string(self):
        txt = ("Texto: %s\n\tpor %s\nItens: %s\nPontos: %d\n" %(self.texto, self.autor, self.itens, self.pontos))
        if self.dependencias != []:
            for ref in range(len(self.dependencias)):
                txt = txt + ("\tReferencia: %s\n" %(self.dependencias[ref].texto))
        return txt