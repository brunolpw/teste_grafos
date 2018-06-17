#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sqlite3

from sugestao import Sugestao
from funcionario import Funcionario
from turma import Turma

"""
    Banco é uma classe que faz a chamada às funções de banco de dados, para
fazer a leitura, gravação, alteração e remoção de sugestões, tem por finalidade
melhorar a usabilidade da aplicação.
"""
class Banco(object):
    def __init__(self):
        self.path = 'banco/sugestao.db'
        self.graph={}
        self.conectando()

    def conectando(self):
        conn = sqlite3.connect(self.path)
        conn.close()

###############################################################################
#   Area de criação de tabelas                                                #
###############################################################################

    def create_table(self):
        sql_sugestoes = """
        CREATE TABLE IF NOT EXISTS sugestoes (
            id     INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            autor  VARCHAR(256),
            titulo  VARCHAR(256),
            texto  VARCHAR(1024),
            itens  VARCHAR(256),
            objetivos VARCHAR(256),
            pontos INTEGER
        );
        """

        # usar criptografia na senha.
        sql_funcionarios = """
        CREATE TABLE IF NOT EXISTS funcionarios (
            id    INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            nome  VARCHAR(256),
            senha VARCHAR(256)
        );
        """

        sql_itens = """
        CREATE TABLE IF NOT EXISTS itens (
            id    INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            nome  VARCHAR(256),
            valor INTEGER
        );
        """

        sql_alunos = """
        CREATE TABLE IF NOT EXISTS alunos (
            id    INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            nome  VARCHAR(256),
            idade INTEGER
        );
        """

        sql_turmas = """
        CREATE TABLE IF NOT EXISTS turmas (
            id           INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            nivel        VARCHAR(15),
            ano          VARCHAR(100)
        );
        """
        #######################################################################
        # Tabelas de relações                                                 #
        #######################################################################
        sql_vertices = """
        CREATE TABLE IF NOT EXISTS vertices (
            id            INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            id_node_pai   INTEGER,
            id_node_filho INTEGER,
            FOREIGN KEY (id_node_pai)   REFERENCES sugestoes(id),
            FOREIGN KEY (id_node_filho) REFERENCES sugestoes(id)
        );
        """

        sql_relacao_turma = """
        CREATE TABLE IF NOT EXISTS relacao_turmas (
            id           INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            id_turma     INTEGER,
            id_tema      INTEGER,
            id_aluno     INTEGER,
            id_professor INTEGER,
            FOREIGN KEY (id_tema) REFERENCES turmas(id),
            FOREIGN KEY (id_tema) REFERENCES sugestoes(id),
            FOREIGN KEY (id_aluno) REFERENCES alunos(id),
            FOREIGN KEY (id_professor) REFERENCES professores(id)
        );
        """

        sql_itens_sugestoes = """
        CREATE TABLE IF NOT EXISTS itens_sugestoes (
            id          INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            id_sugestao INTEGER,
            id_item     INTEGER,
            FOREIGN KEY (id_sugestao)   REFERENCES sugestoes(id),
            FOREIGN KEY (id_item) REFERENCES itens(id)
        );
        """

        conn = sqlite3.connect(self.path)
        cursor = conn.cursor()
        #sqlite3.Warning: You can only execute one statement at a time.
        # Apenas uma query por vez.
        cursor.execute(sql_sugestoes)
        cursor.execute(sql_funcionarios)
        cursor.execute(sql_itens)
        cursor.execute(sql_alunos)
        cursor.execute(sql_turmas)

        cursor.execute(sql_vertices)
        cursor.execute(sql_relacao_turma)
        cursor.execute(sql_itens_sugestoes)
        
        conn.close()

###############################################################################
#   Area de inserts                                                           #
###############################################################################

    def insert_sugest(self, Sugestao):
        conn = sqlite3.connect(self.path)
        cursor = conn.cursor()
        cursor.execute("""
        INSERT INTO sugestoes (autor, titulo, texto, itens, objetivos, pontos) VALUES (?, ?, ?, ?, ?, ?);
        """, (str(Sugestao.autor), str(Sugestao.titulo), str(Sugestao.texto), str(Sugestao.itens), str(Sugestao.objetivos), Sugestao.pontos))
        #("Autor 17", "Titulo 17", "Texto 17", str([]), str([]), 17))
        
        conn.commit()
        conn.close()
    
    def insert_funcionarios(self, funcionario):
        conn = sqlite3.connect(self.path)
        cursor = conn.cursor()
        cursor.execute("""
        INSERT INTO funcionarios (nome, senha) VALUES (?, ?);
        """, (funcionario.nome, funcionario.senha))
        conn.commit()
        conn.close()

    def insert_itens(self, item):
        conn = sqlite3.connect(self.path)
        cursor = conn.cursor()
        cursor.execute("""
        INSERT INTO itens (nome, valor) VALUES (?, ?);
        """, (item.nome, item.valor))
        conn.commit()
        conn.close()

    def insert_alunos(self, aluno):
        conn = sqlite3.connect(self.path)
        cursor = conn.cursor()
        cursor.execute("""
        INSERT INTO alunos (nome, idade) VALUES (?, ?);
        """, (aluno.nome, aluno.idade))
        conn.commit()
        conn.close()

    def insert_turmas(self, turma):
        conn = sqlite3.connect(self.path)
        cursor = conn.cursor()
        cursor.execute("""
        INSERT INTO turmas (nivel, ano) VALUES (?, ?);
        """, (turma.nivel, turma.ano))
        conn.commit()
        conn.close()

    def insert_node_sugest(self, sug1, sug2):
        conn = sqlite3.connect(self.path)
        cursor = conn.cursor()
        cursor.execute("""
        INSERT INTO vertices (id_node_pai, id_node_filho) VALUES (?, ?);
        """, (sug1.id, sug2.id))
        conn.commit()
        conn.close()

    def insert_relacao_turmas(self, turma, tema, professor, aluno):
        conn = sqlite3.connect(self.path)
        cursor = conn.cursor()
        cursor.execute("""
        INSERT INTO relacao_turmas (id_turma, id_tema, id_aluno, id_professor) VALUES (?, ?, ?, ?);
        """, (turma.id, tema.id, professor.id, aluno.id))
        conn.commit()
        conn.close()

    def insert_itens_sugestoes(self, sug, item):
        conn = sqlite3.connect(self.path)
        cursor = conn.cursor()
        cursor.execute("""
        INSERT INTO itens_sugestoes (id_sugestao, id_item) VALUES (?, ?);
        """, (sug.id, item.id))
        conn.commit()
        conn.close()

###############################################################################
#   Area de updates                                                           #
###############################################################################

    def update_sugest(self, Sugestao, this_id):
        conn = sqlite3.connect(self.path)
        cursor = conn.cursor()
        cursor.execute("""
        UPDATE sugestoes
        SET texto=?, autor=?, itens=?, pontos=?
        WHERE id = ?;
        """, (Sugestao.texto, Sugestao.autor, str(Sugestao.itens), Sugestao.pontos, this_id))
        conn.commit()
        conn.close()

###############################################################################
#   Area de retornos                                                           #
###############################################################################
    def read_sugest(self):
        conn = sqlite3.connect(self.path)
        cursor = conn.cursor()
        cursor.execute("""
        SELECT * FROM sugestoes;
        """)
        for linha in cursor.fetchall():
            print(linha)
        conn.close()

    def read_by_id_sugest(self, id=0):
        conn = sqlite3.connect(self.path)
        cursor = conn.cursor()
        cursor.execute("""
        SELECT * FROM sugestoes WHERE id = %d;
        """ %id)
        for linha in cursor.fetchall():
            return linha
        conn.close()
    """
    SELECT p.autor AS autor_pai,
       (SELECT q.autor
          FROM sugestoes AS q
         WHERE q.id = e.id_node_filho) AS autor_filho
  FROM vertices AS e, sugestoes AS p
 WHERE e.id_node_pai = p.id 


SELECT p.autor AS autor_pai, (SELECT q.autor FROM sugestoes AS q WHERE q.id = e.id_node_filho) AS autor_filho FROM vertices AS e, sugestoes AS p WHERE e.id_node_pai = p.id AND p.id = 2;
    """
    def read_path(self, sug):
        conn = sqlite3.connect(self.path)
        cursor = conn.cursor()
        cursor.execute("""
        SELECT p.autor AS autor_pai, (
            SELECT q.autor FROM sugestoes AS q WHERE q.id = e.id_node_filho
            ) AS autor_filho
        FROM vertices AS e, sugestoes AS p
        WHERE e.id_node_pai = p.id AND p.id = %d;
        """ %sug.id)
        nodes = []
        for linha in cursor.fetchall():
            nodes.append(linha[1])
        conn.close()
        return nodes

###############################################################################
#   Area de logicas                                                           #
###############################################################################

    """
        Converte os valores retornados do banco em Sugestao.
    """
    def convert_data(self, data):
        sug = Sugestao()
        sug.id        = data[0]
        sug.autor     = data[1]
        sug.titulo    = data[2]
        sug.texto     = data[3]
        sug.itens     = data[4]
        sug.objetivos = data[5]
        sug.pontos    = data[6]
        return sug

    """
        Cria um grafo com os valores retornados do banco.
    """
    def create_graph(self, sug1):
        aux = self.read_by_id_sugest(sug1.id)
        sug = self.convert_data(aux)
        #dict_sugs={}
        self.graph[sug.autor] = self.read_path(sug1)
        return self.graph

    """
        Verifica quantas dependencias há em determinada sugestão.
    """
    def verifica_dependencias(self, sug):
        #aux = self.convert_data(self.read_by_id_sugest(sug.id))
        conn = sqlite3.connect(self.path)
        cursor = conn.cursor()
        cursor.execute("""
        SELECT COUNT(*) FROM vertices WHERE id_node_pai = %d;
        """ %sug.id)
        result = cursor.fetchone()[0]
        #aux.remove_pontos(result)
        conn.close()
        #self.update_sugest(aux, aux.id)
        return result

    def lista_sem_dependencias(self):
        conn = sqlite3.connect(self.path)
        cursor = conn.cursor()
        cursor.execute("""
        SELECT *
        FROM sugestoes
        EXCEPT
        SELECT s.*
        FROM sugestoes AS s
        INNER JOIN vertices AS v ON v.id_node_pai = s.id;
        """)
        for linha in cursor.fetchall():
            sug = self.convert_data(linha)
            print(sug.autor, sug.pontos)
        conn.close()

    def lista_com_dependencias(self):
        conn = sqlite3.connect(self.path)
        cursor = conn.cursor()
        cursor.execute("""
        SELECT DISTINCT s.*
        FROM sugestoes AS s
        LEFT JOIN vertices AS v
        WHERE s.id = v.id_node_pai;
        """)
        for linha in cursor.fetchall():
            sug = self.convert_data(linha)
            print(sug.autor)
        conn.close()

    """
        Lista todos os itens pela ordem de sua pontuação (desprezando o valor
    atualizado com base em suas dependencias).
    """
    def read_all_order_by_pontos(self):
        sug       = Sugestao()
        sugestoes = []
        conn      = sqlite3.connect(self.path)
        cursor    = conn.cursor()
        cursor.execute("""
        SELECT * FROM sugestoes ORDER BY pontos DESC;
        """)
        for linha in cursor.fetchall():
            sug = self.convert_data(linha)
            sugestoes.append(sug)
            #print(linha)
        conn.close()
        return sugestoes

    """
        Retorna a soma de pontos de todas as sugestões do banco.
    """
    def read_sum_pontos_from_sugestoes(self):
        conn      = sqlite3.connect(self.path)
        cursor    = conn.cursor()
        cursor.execute("""
        SELECT sum(pontos) FROM sugestoes;
        """)
        sum_sugs = cursor.fetchone()
        conn.close()
        return sum_sugs[0]
