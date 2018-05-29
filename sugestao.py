#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    Sugestão é uma classe basica para representar as opões que serão lançadas
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
        self.ref_sugestao = []

    def add_ponto(self, ponto=0):
        self.pontos = self.pontos + ponto
        if self.ref_sugestao != None:
            self.pontos = self.pontos - len(self.ref_sugestao)

    def add_item(self, item=[]):
        self.itens.append(item)

    def add_referencias(self, ref=[]):
        self.ref_sugestao.append(ref)

    def find_id(self, id=0):
        if id == self.id:
            return to_string()
        return "nenhum id encontrado."

    def to_string(self):
        txt = ("Texto: %s\n\tpor %s\nItens: %s\nPontos: %d\n" %(self.texto, self.autor, self.itens, self.pontos))
        if self.ref_sugestao != []:
            for ref in range(len(self.ref_sugestao)):
                txt = txt + ("\tReferencia: %s\n" %(self.ref_sugestao[ref].texto))
        return txt