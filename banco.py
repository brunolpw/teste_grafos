#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sqlite3

from sugestao import Sugestao

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

    def create_table(self):
        sql_sugestoes = """
        CREATE TABLE IF NOT EXISTS sugestoes (
            id     INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            texto  VARCHAR(256),
            autor  VARCHAR(256),
            itens  VARCHAR(256),
            pontos INTEGER
        );
        """

        sql_vertices = """
        CREATE TABLE IF NOT EXISTS vertices (
            id            INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            id_node_pai   INTEGER,
            id_node_filho INTEGER,
            FOREIGN KEY (id_node_pai)   REFERENCES sugestoes(id),
            FOREIGN KEY (id_node_filho) REFERENCES sugestoes(id)
        );
        """

        conn = sqlite3.connect(self.path)
        cursor = conn.cursor()
        #sqlite3.Warning: You can only execute one statement at a time.
        cursor.execute(sql_sugestoes)
        cursor.execute(sql_vertices)
        conn.close()

    def insert_sugest(self, Sugestao):
        conn = sqlite3.connect(self.path)
        cursor = conn.cursor()
        cursor.execute("""
        INSERT INTO sugestoes (texto, autor, itens, pontos) VALUES (?, ?, ?, ?);
        """, (Sugestao.texto, Sugestao.autor, str(Sugestao.itens), Sugestao.pontos))
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
            #print(linha)
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
        #path = []
        for linha in cursor.fetchall():
            #print(linha)
            #list(linha)

            nodes.append(linha[1])
            #' '.join(linha)
#            for node in nodes:
#                print("Node: %s" %node)
#                if node not in path:
#                    new_path = self.read_path(node)
#                    if new_path: return new_path
        conn.close()
        return nodes
    """
        Criar uma função que leia o valor individual de cada sugestão pega
    na lista anterior, afim de que esta seja adicionada a um dicionário que
    representará o grafo.

    new = Sugestao()
    new_s = b.read_by_id_sugest(2)
    new.id     = new_s[0]
    new.texto  = new_s[1]
    new.autor  = new_s[2]
    new.itens  = new_s[3]
    new.pontos = new_s[4]
    print("new.to_string()")
    print(new.to_string())
    """

    def convert_data(self, data):
        sug = Sugestao()
        sug.id     = data[0]
        sug.texto  = data[1]
        sug.autor  = data[2]
        sug.itens  = data[3]
        sug.pontos = data[4]
        return sug

    def create_graph(self, sug1):
        #sug = Sugestao()
        aux = self.read_by_id_sugest(sug1.id)
        sug = self.convert_data(aux)
        dict_sugs={}
        #sug.id     = aux[0]
        #sug.texto  = aux[1]
        #sug.autor  = aux[2]
        #sug.itens  = aux[3]
        #sug.pontos = aux[4]

        #dict_sugs[sug.autor]= self.read_path(sug1)
        #return dict_sugs
        self.graph[sug.autor] = self.read_path(sug1)
        return self.graph
