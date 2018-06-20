#!/usr/bin/env python
# -*- coding: utf-8 -*-

from sugestao    import Sugestao
from item        import Item
from aluno       import Aluno
from funcionario import Funcionario
from turma       import Turma
from grafos      import Grafos
from banco       import Banco
from selecao     import Selecao

"""
    Rodando o sistema.
"""
def run():
    """
        Instancias
    """
    s1 = Sugestao(1, "Primeiro tema", "autor 1", [], 0)
    s2 = Sugestao(2, "Segundo tema",  "autor 2", [], 0)
    s3 = Sugestao(3, "Terceiro tema", "autor 3", [], 0)
    s4 = Sugestao(4, "Quarto tema",   "autor 4", [], 7)
    s5 = Sugestao(5, "Quinto tema",   "autor 5", [], 0)
    
    s1.add_ponto(5)
    s2.add_ponto(7)
    s3.add_ponto(3)
    s4.add_ponto(2)
    s5.add_ponto(15)

    s1.add_item(['a', 'b', 'c'])
    s2.add_item(['1', '2', '3'])
    s3.add_item([1, 2, 3])
    s4.add_item(['&', '%', '@'])
    s5.add_item(['#', 'B', 3])

    s1.add_item(['x', 'y', 'z'])

    #print(s1.to_string())
    #print(s2.to_string())
    #print(s3.to_string())
    #print(s4.to_string())
    #print(s5.to_string())

    # Grafos
    g = Grafos()

    #g.add_sugestao(s1) # id: 1
    #g.add_sugestao(s2) # id: 2 duas tReferencias (s3 e s5)
    #g.add_sugestao(s3) # id: 3
    #g.add_sugestao(s4) # id: 4 uma tReferencia (s2)
    #g.add_sugestao(s5) # id: 5

    """
        Exemplo de grafos.
    """
    """
    graph = {'A' : ['B', 'C'],
             'B' : ['C', 'D'],
             'C' : ['D', 'F'],
             'D' : ['C'],
             'E' : ['F'],
             'F' : ['C'],
             }
    """
    #print("find path")
    #print("A -> D: %s" %g.find_path(graph, 'A', 'D')) # ['A', 'B', 'C', 'D']
    #print("A -> F: %s" %g.find_path(graph, 'A', 'F')) # ['A', 'B', 'C', 'F']

    #print("find all paths")
    #print("A -> D: %s" %g.find_all_paths(graph, 'A', 'D')) # [['A', 'B', 'C', 'D'], ['A', 'B', 'D'], ['A', 'C', 'D']]
    #print("A -> F: %s" %g.find_all_paths(graph, 'A', 'F')) # [['A', 'B', 'C', 'F'], ['A', 'B', 'D', 'C', 'F'], ['A', 'C', 'F']]

    #print("find shortest path")
    #print("A -> D: %s" %g.find_shortest_path(graph, 'A', 'D')) # ['A', 'B', 'D']
    #print("A -> F: %s" %g.find_shortest_path(graph, 'A', 'F')) # ['A', 'C', 'F']

    #print(g.sugs)
    #print("4 -> 5: %s" %g.find_path(g.sugs, 4, 5)) # [4, 2, 5]

    #for a in g.find_path(g.sugs, 4, 5):
    #    s = Sugestao()
        #s = g.sugs[4]
    #    print(a)
    #    print(s.find_id(a))
    #s2.add_referencias(3)
    #s2.add_referencias(5)
    #s4.add_referencias(2)
    
    b = Banco()



    print("Todos elementos do banco.")
    b.read_path(s1)

#    b.read_sugest()
#    print("\n\n")
#    b.read_by_id_sugest(3)

#    s_aux = s2
#    s_aux.pontos = 15
#    b.update_sugest(s_aux, 2)
#    b.read_by_id_sugest(2)

    b.create_graph(s1)
    b.create_graph(s2)
    b.create_graph(s3)
    
    #print(b.create_graph(s1))
    print(b.graph)
    print("find path")
    print("autor 1 -> autor 5: %s" %g.find_path(b.graph, 'autor 1', 'autor 5')) # ['autor 1', 'autor 2', 'autor 3', 'autor 5']
    print(b.verifica_dependencias(s2))
    #print(b.read_by_id_sugest(2))
    #for a in new_s.ref_sugestao:
    #    print(a)
###############################################################################
###############################################################################
###############################################################################
###############################################################################
###############################################################################
def teste():
    b = Banco()
    g = Grafos()

    """
        Instancias
    """
    s1 = Sugestao(1, "Primeiro tema", "autor 1", [], 0)
    s2 = Sugestao(2, "Segundo tema",  "autor 2", [], 0)
    s3 = Sugestao(3, "Terceiro tema", "autor 3", [], 0)
    s4 = Sugestao(4, "Quarto tema",   "autor 4", [], 7)
    s5 = Sugestao(5, "Quinto tema",   "autor 5", [], 0)

    s6  = Sugestao(6, "Sexto tema",             "autor 6", [], 0)
    s7  = Sugestao(7, "Setimo tema",            "autor 7", [], 0)
    s8  = Sugestao(8, "Oitavo tema",            "autor 8", [], 0)
    s9  = Sugestao(9, "Nono tema",              "autor 9", [], 0)
    s10 = Sugestao(10, "Decimo tema",           "autor 10", [], 0)
    s11 = Sugestao(11, "Decimo Primeiro tema", "autor 11", [], 0)
    s12 = Sugestao(12, "Decimo Segundo tema",  "autor 12", [], 0)
    s13 = Sugestao(13, "Decimo Terceiro tema", "autor 13", [], 0)
    s14 = Sugestao(14, "Decimo Quarto tema",   "autor 14", [], 0)
    s15 = Sugestao(15, "Decimo Quinto tema",   "autor 15", [], 0)

    s1.add_ponto(5)
    s2.add_ponto(7)
    s3.add_ponto(3)
    s4.add_ponto(2)
    s5.add_ponto(15)

    s6.add_ponto(10)
    s7.add_ponto(7)
    s8.add_ponto(12)
    s9.add_ponto(13)
    s10.add_ponto(42)
    s11.add_ponto(4)
    s12.add_ponto(5)
    s13.add_ponto(18)
    s14.add_ponto(20)
    s15.add_ponto(5)
    """
    s1.add_item(['a', 'b', 'c'])
    #s2.add_item(['1', '2', '3'])
    s3.add_item([1, 2, 3])
    s4.add_item(['&', '%', '@'])
    s5.add_item(['#', 'B', 3])

    s6.add_item(['x', 'y', 'z'])
    s7.add_item(['X', 'Y', 'Z'])
    s8.add_item(['1', 2, 'c'])
    s9.add_item(['a', '%', '@', '#'])
    s10.add_item(['a', 'b', 'c', 'd', 'e', 'f'])
    s11.add_item(['1', '2', '3', '4', '5'])
    s12.add_item([1, 2, 3, 4, 5])
    s13.add_item(['$', 'B', '#'])
    s14.add_item([1, '!', '@'])
    s15.add_item(['Q', 'W', 'E', 'R', 'T'])

    s1.add_item(['x', 'y', 'z'])
    #s2.add_item(['4', '5', '6'])
    
    b.update_sugest(s1, s1.id)
    #b.update_sugest(s2, s2.id)
    b.update_sugest(s3, s3.id)
    b.update_sugest(s4, s4.id)
    b.update_sugest(s5, s5.id)
    b.update_sugest(s6, s6.id)
    b.update_sugest(s7, s7.id)
    b.update_sugest(s8, s8.id)
    b.update_sugest(s9, s9.id)
    b.update_sugest(s10, s10.id)
    b.update_sugest(s11, s11.id)
    b.update_sugest(s12, s12.id)
    b.update_sugest(s13, s13.id)
    b.update_sugest(s14, s14.id)
    b.update_sugest(s15, s15.id)
    """

    b.read_path(s1)
    b.create_graph(s1)
    b.create_graph(s2)
    b.create_graph(s3)

    print("graph")
    print(b.graph)
    print("\n")
    print("find_path")
    print("autor 1 -> autor 5: %s\n" %g.find_path(b.graph, 'autor 1', 'autor 5')) # ['autor 1', 'autor 2', 'autor 3', 'autor 5']
    
    print("find_all_paths")
    print("autor 1 -> autor 5: %s\n" %g.find_all_paths(b.graph, 'autor 1', 'autor 5')) # [['autor 1', 'autor 2', 'autor 3', 'autor 5'], ['autor 1', 'autor 2', 'autor 5'], ['autor 1', 'autor 3', 'autor 5']]
    
    print("find_shortest_path")
    print("autor 1 -> autor 5: %s\n" %g.find_shortest_path(b.graph, 'autor 1', 'autor 5')) # ['autor 1', 'autor 2', 'autor 5']
    
    print("b.verifica_dependencias(s2)")
    print(b.verifica_dependencias(s2))
    print("b.lista_com_dependencias()")
    #print(b.lista_com_dependencias())
    b.lista_com_dependencias()
    print("b.lista_sem_dependencias()")
    #print(b.lista_sem_dependencias())
    b.lista_sem_dependencias()
###############################################################################
###############################################################################
###############################################################################
###############################################################################
###############################################################################
def inserindo_dados_no_banco():
    b = Banco()

# criando registros.
    s1 = Sugestao(1,"autor 1", "Titulo 1", "Tema 1", [], [], 10)
    s2 = Sugestao(2,"autor 2", "Titulo 2", "Tema 2", [], [],  7)
    s3 = Sugestao(3,"autor 3", "Titulo 3", "Tema 3", [], [], 20)
    s4 = Sugestao(4,"autor 4", "Titulo 4", "Tema 4", [], [], 30)
    s5 = Sugestao(5,"autor 5", "Titulo 5", "Tema 5", [], [], 25)

    s6  = Sugestao(6, "autor 6",  "Titulo 6",  "Tema 6",  [], [], 18)
    s7  = Sugestao(7, "autor 7",  "Titulo 7",  "Tema 7",  [], [],  5)
    s8  = Sugestao(8, "autor 8",  "Titulo 8",  "Tema 8",  [], [],  3)
    s9  = Sugestao(9, "autor 9",  "Titulo 9",  "Tema 9",  [], [], 11)
    s10 = Sugestao(10,"autor 10", "Titulo 10", "Tema 10", [], [], 42)

    s11 = Sugestao(11,"autor 11", "Titulo 11", "Tema 11", [], [], 15)
    s12 = Sugestao(12,"autor 12", "Titulo 12", "Tema 12", [], [], 35)
    s13 = Sugestao(13,"autor 13", "Titulo 13", "Tema 13", [], [], 13)
    s14 = Sugestao(14,"autor 14", "Titulo 14", "Tema 14", [], [], 15)
    s15 = Sugestao(15,"autor 15", "Titulo 15", "Tema 15", [], [],  8)
    
    i1 = Item(1, "item 1",  "5")
    i2 = Item(2, "item 2",  "9")
    i3 = Item(3, "item 3",  "4")
    i4 = Item(4, "item 4", "12")
    i5 = Item(5, "item 5",  "2")
    
    i6  = Item(6,  "item 6",   "8")
    i7  = Item(7,  "item 7",  "42")
    i8  = Item(8,  "item 8",   "3")
    i9  = Item(9,  "item 9",   "7")
    i10 = Item(10, "item 10", "15")

    a1 = Aluno(1, "aluno 1", 2)
    a2 = Aluno(2, "aluno 2", 2)
    a3 = Aluno(3, "aluno 3", 3)
    a4 = Aluno(4, "aluno 4", 3)
    a5 = Aluno(5, "aluno 5", 1)

    f1 = Funcionario(1, "funcionario 1", "funcionario 1")
    f2 = Funcionario(2, "funcionario 2", "funcionario 2")
    f3 = Funcionario(3, "funcionario 3", "funcionario 3")
    f4 = Funcionario(4, "funcionario 4", "funcionario 4")
    f5 = Funcionario(5, "funcionario 5", "funcionario 5")

    t1 = Turma(1, "nivel 1", "2018")
    t2 = Turma(2, "nivel 2", "2018")
    t3 = Turma(3, "nivel 3", "2018")
    t4 = Turma(4, "nivel 4", "2018")

# inserindo registros no banco.
    print("Criando tabelas...")
    b.create_table()

    print("Tabelas criadas.")
    print("Inserindo dados em 'sugestoes'...")
    b.insert_sugest(s1)
    b.insert_sugest(s2)
    b.insert_sugest(s3)
    b.insert_sugest(s4)
    b.insert_sugest(s5)
    b.insert_sugest(s6)
    b.insert_sugest(s7)
    b.insert_sugest(s8)
    b.insert_sugest(s9)
    b.insert_sugest(s10)
    b.insert_sugest(s11)
    b.insert_sugest(s12)
    b.insert_sugest(s13)
    b.insert_sugest(s14)
    b.insert_sugest(s15)
    print("Dados inseridos.")
    print("Inserindo dados em 'vertices'...")
# Criar ar relações de s1
    b.insert_node_sugest(s1, s2)
    b.insert_node_sugest(s1, s3)
# Criar ar relações de s2
    b.insert_node_sugest(s2, s3)
    b.insert_node_sugest(s2, s4)
    b.insert_node_sugest(s2, s5)
# Criar ar relações de s3
    b.insert_node_sugest(s3, s5)
# Criar ar relações de s7
    b.insert_node_sugest(s7, s4)
    b.insert_node_sugest(s7, s5)
    b.insert_node_sugest(s7, s6)
# Criar ar relações de s11
    b.insert_node_sugest(s11, s7)
    b.insert_node_sugest(s11, s8)
# Criar ar relações de s13
    b.insert_node_sugest(s13, s1)
    b.insert_node_sugest(s13, s2)
    b.insert_node_sugest(s13, s3)
    b.insert_node_sugest(s13, s4)
    b.insert_node_sugest(s13, s5)
    print("Dados inseridos.")
    print("Inserindo dados em 'itens'...")
    b.insert_itens(i1)
    b.insert_itens(i2)
    b.insert_itens(i3)
    b.insert_itens(i4)
    b.insert_itens(i5)
    b.insert_itens(i6)
    b.insert_itens(i7)
    b.insert_itens(i8)
    b.insert_itens(i9)
    b.insert_itens(i10)
    print("Dados inseridos.")
    print("Inserindo dados em 'alunos'...")
    b.insert_alunos(a1)
    b.insert_alunos(a2)
    b.insert_alunos(a3)
    b.insert_alunos(a4)
    b.insert_alunos(a5)
    print("Dados inseridos.")
    print("Inserindo dados em 'funcionarios'...")
    b.insert_funcionarios(f1)
    b.insert_funcionarios(f2)
    b.insert_funcionarios(f3)
    b.insert_funcionarios(f4)
    b.insert_funcionarios(f5)
    print("Dados inseridos.")
    print("Inserindo dados em 'turmas'...")
    b.insert_turmas(t1)
    b.insert_turmas(t2)
    b.insert_turmas(t3)
    b.insert_turmas(t4)
    print("Dados inseridos.")
    print("Inserindo dados em 'relacao_turmas'...")
    b.insert_relacao_turmas(t1, s1, f1, a1)
    b.insert_relacao_turmas(t1, s1, f1, a2)
    b.insert_relacao_turmas(t1, s1, f1, a3)

    b.insert_relacao_turmas(t2, s5, f2, a5)
    b.insert_relacao_turmas(t2, s5, f2, a4)
    b.insert_relacao_turmas(t2, s5, f2, a3)

    b.insert_relacao_turmas(t3, s7, f5, a2)
    b.insert_relacao_turmas(t3, s7, f5, a4)
    b.insert_relacao_turmas(t3, s7, f5, a5)

    b.insert_relacao_turmas(t4, s3, f3, a1)
    b.insert_relacao_turmas(t4, s3, f3, a3)
    b.insert_relacao_turmas(t4, s3, f3, a5)
    print("Dados inseridos.")
    print("Inserindo dados em 'insert_itens_sugestoes'...")
# sugestões = 1~15
# itens = 1~10
    b.insert_itens_sugestoes(s1, i1)
    b.insert_itens_sugestoes(s1, i2)
    b.insert_itens_sugestoes(s1, i3)
    b.insert_itens_sugestoes(s1, i4)
    b.insert_itens_sugestoes(s1, i5)
    b.insert_itens_sugestoes(s1, i6)
    b.insert_itens_sugestoes(s1, i7)

    b.insert_itens_sugestoes(s2, i8)
    b.insert_itens_sugestoes(s2, i9)
    b.insert_itens_sugestoes(s2, i10)

    b.insert_itens_sugestoes(s3, i1)
    b.insert_itens_sugestoes(s3, i3)
    b.insert_itens_sugestoes(s3, i5)
    b.insert_itens_sugestoes(s3, i7)
    b.insert_itens_sugestoes(s3, i9)

    b.insert_itens_sugestoes(s4, i2)
    b.insert_itens_sugestoes(s4, i4)
    b.insert_itens_sugestoes(s4, i6)
    b.insert_itens_sugestoes(s4, i8)
    b.insert_itens_sugestoes(s4, i10)

    b.insert_itens_sugestoes(s5, i1)
    b.insert_itens_sugestoes(s5, i4)
    b.insert_itens_sugestoes(s5, i7)

    b.insert_itens_sugestoes(s6, i1)

    b.insert_itens_sugestoes(s7, i3)
    b.insert_itens_sugestoes(s7, i5)
    b.insert_itens_sugestoes(s7, i7)

    b.insert_itens_sugestoes(s8, i10)

    b.insert_itens_sugestoes(s9, i1)
    b.insert_itens_sugestoes(s9, i10)

    b.insert_itens_sugestoes(s10, i10)

    b.insert_itens_sugestoes(s11, i1)
    b.insert_itens_sugestoes(s11, i2)
    b.insert_itens_sugestoes(s11, i3)

    b.insert_itens_sugestoes(s12, i4)
    b.insert_itens_sugestoes(s12, i5)
    b.insert_itens_sugestoes(s12, i6)

    b.insert_itens_sugestoes(s13, i5)
    b.insert_itens_sugestoes(s13, i6)
    b.insert_itens_sugestoes(s13, i7)

    b.insert_itens_sugestoes(s14, i4)
    b.insert_itens_sugestoes(s14, i7)
    b.insert_itens_sugestoes(s14, i9)

    b.insert_itens_sugestoes(s15, i1)
    b.insert_itens_sugestoes(s15, i2)
    b.insert_itens_sugestoes(s15, i3)
    b.insert_itens_sugestoes(s15, i4)
    b.insert_itens_sugestoes(s15, i5)
    print("Dados inseridos.")
    print("Tudo pronto.")

def projeto():
    #inserindo_dados_no_banco()
    s = Selecao()
    print(s.roleta())

###############################################################################
###############################################################################
###############################################################################
###############################################################################
###############################################################################
"""
    Faz a chamada para este mesmo arquivo.
"""
if __name__ == "__main__":

    for i in range(9):
        projeto()
    #run()
    #teste()
    #"""
    """
    sug = Sugestao()
    s = Selecao()
    s.seleciona(4) # default 5
    

    #a = sorted(s.new_sugs, key=attrgetter('pontos'))
    #sorted(student_objects, key=attrgetter('grade', 'age'))
    for i in s.new_sugs:
        print(i.to_string())
    print("\nmelhor")
    print(s.pega_melhor())
    """
    #"""
