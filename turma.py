#!/usr/bin/env python
# -*- coding: utf-8 -*-

from sugestao    import Sugestao
from aluno       import Aluno
from funcionario import Funcionario
"""

"""
class Turma(object):
    def __init__(self, id=0, nivel='', ano=''):
        self.id          = id
        self.nivel       = nivel
        self.ano         = ano
        self.sugestao    = Sugestao
        self.alunos      = []
        self.professor = Funcionario
    
    def add_aluno(self, aluno):
        if type(aluno) == list:
            for a in aluno:
                self.alunos.append(a)
        else:
            self.alunos.append(aluno)

    def to_string(self):
        return ("turma %s de %d.\n prof.: \n assunto: " %(self.nivel, self.ano))