#!/usr/bin/env python
# -*- coding: utf-8 -*-

import datetime

from item import Item

"""
    Sugestão é uma classe basica para representar as opções que serão lançadas
pelos professores e que o sistema usará para sugerir de tema para uso em sala
de aula.
"""
class Sugestao(object):
    def __init__(self, id=0, autor='', titulo='', texto='', pontos=0):
        self.id           = id
        self.autor        = autor
        self.titulo       = titulo
        self.texto        = texto
        self.pontos       = pontos
        self.data_criacao = 0
        self.ultimo_uso   = 0 
        self.prof_atual   = ''
        self.objetivos    = []
        self.itens        = []
        self.dependencias = []

    def add_ponto(self, ponto=0):
        self.pontos = self.pontos + ponto
        #if self.dependencias != None:
        #    self.pontos = self.pontos - len(self.dependencias)

    def remove_pontos(self, pontos=0):
        self.pontos = self.pontos - pontos
        if self.pontos <= 0:
            self.pontos = 0

    def add_itens(self, ref):
        if type(ref) == list:
            for i in ref:
                #i = Item()
                self.itens.append(i.to_string())
        else:
            #ref = Item()
            self.itens.append(ref.to_string())

    def add_dependencias(self, ref):
        if type(ref) == list:
            for i in ref:
                self.dependencias.append(i)
        else:
            self.dependencias.append(ref)

    def to_string(self):
        txt = ("titulo: %s\n\tpor %s\ndescrição: %s\nPontos: %d\n" %(self.titulo, self.autor, self.texto, self.pontos))
        if self.itens != []:
            for ref in range(len(self.itens)):
                txt = txt + ("Item %d: %s\n" %(ref+1, self.itens[ref]))
        if self.dependencias != []:
            for ref in range(len(self.dependencias)):
                txt = txt + ("Dependencia %d: %s\n" %(ref+1, self.dependencias[ref]))
        return txt