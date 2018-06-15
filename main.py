#!/usr/bin/env python
# -*- coding: utf-8 -*-

from sugestao import Sugestao
from grafos   import Grafos
from banco    import Banco
from selecao  import Selecao

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

#    b.create_table() # texto, autor, itens, pontos
#    print("\n\n")
#    b.insert_sugest(s1)
#    b.insert_sugest(s2)
#    b.insert_sugest(s3)
#    b.insert_sugest(s4)
#    b.insert_sugest(s5)

#    b.insert_node_sugest(s1, s2)
#    b.insert_node_sugest(s1, s3)

#    b.insert_node_sugest(s2, s3)
#    b.insert_node_sugest(s2, s4)
#    b.insert_node_sugest(s2, s5)

#    b.insert_node_sugest(s3, s5)

    print("Todos elementos do banco.")
    b.read_path(s1)

#    b.read_sugest()
#    print("\n\n")
#    b.read_by_id_sugest(3)

#    s_aux = s2
#    s_aux.pontos = 15
#    b.update_sugest(s_aux, 2)
#    b.read_by_id_sugest(2)
    
    """
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
    
    #b.insert_sugest(s6)
    #b.insert_sugest(s7)
    #b.insert_sugest(s8)
    #b.insert_sugest(s9)
    #b.insert_sugest(s10)
    #b.insert_sugest(s11)
    #b.insert_sugest(s12)
    #b.insert_sugest(s13)
    #b.insert_sugest(s14)
    #b.insert_sugest(s15)

    #b.insert_node_sugest(s7, s4)
    #b.insert_node_sugest(s7, s5)
    #b.insert_node_sugest(s7, s6)

    #b.insert_node_sugest(s11, s7)
    #b.insert_node_sugest(s11, s8)

    #b.insert_node_sugest(s13, s1)
    #b.insert_node_sugest(s13, s2)
    #b.insert_node_sugest(s13, s3)
    #b.insert_node_sugest(s13, s4)
    #b.insert_node_sugest(s13, s5)

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
def bancos():
    b = Banco()
    b.create_table()

    
def projeto():
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
