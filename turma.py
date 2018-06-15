#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""

"""
class Turma(object):
    def __init__(self, id=0, nivel='', ano='', tema='', alunos=[], professor=''):
        self.id        = id
        self.nivel     = nivel
        self.ano       = ano
        self.tema      = tema
        self.alunos    = alunos
        self.professor = professor

def to_string(self):
    return ("turma %s de %d.\n prof.: %s\n assunto: %s" %(self.nivel, self.ano, self.professor.nome, self.tema.titulo))