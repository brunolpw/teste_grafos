#!/usr/bin/env python
# -*- coding: utf-8 -*-

import datetime

"""
    Sugestão é uma classe basica para representar as opções que serão lançadas
pelos professores e que o sistema usará para sugerir de tema para uso em sala
de aula.
"""
class Sugestao(object):
    def __init__(self, id=0, titulo='', texto='', autor='', itens=[], objetivos=[], pontos=0):
        self.id           = id
        self.titulo       = titulo
        self.autor        = autor
        self.data_criacao = 0
        self.ultimo_uso   = 0
        self.texto        = texto 
        self.prof_atual   = ''
        self.itens        = itens
        self.objetivos    = objetivos
        self.pontos       = pontos
        self.dependencias = []

    def add_ponto(self, ponto=0):
        self.pontos = self.pontos + ponto
        if self.dependencias != None:
            self.pontos = self.pontos - len(self.dependencias)

    def remove_pontos(self, pontos=0):
        self.pontos = self.pontos - pontos
        if self.pontos <= 0:
            self.pontos = 0

    def add_item(self, item):
        if type(item) == list:
            for i in item:
                self.itens.append(i)
        else:
            self.itens.append(item)

    def add_dependencias(self, ref):
        if type(ref) == list:
            for i in ref:
                self.dependencias.append(i)
        else:
            self.dependencias.append(ref)

    def to_string(self):
        txt = ("titulo: %s\n\tpor %s\ndescrição: %s\nItens: %s\nPontos: %d\n" %(self.titulo, self.autor, self.texto, self.itens, self.pontos))
        if self.dependencias != []:
            for ref in range(len(self.dependencias)):
                txt = txt + ("dependencias %d: %s\n" %(ref+1, self.dependencias[ref]))
        return txt