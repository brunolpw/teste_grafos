#!/usr/bin/env python
# -*- coding: utf-8 -*-

from sugestao import Sugestao
from grafos   import Grafos
from banco    import Banco

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

    g.add_sugestao(s1) # id: 1
    g.add_sugestao(s2) # id: 2 duas tReferencias (s3 e s5)
    g.add_sugestao(s3) # id: 3
    g.add_sugestao(s4) # id: 4 uma tReferencia (s2)
    g.add_sugestao(s5) # id: 5

    """
        Exemplo de grafos.
    """
    graph = {'A' : ['B', 'C'],
             'B' : ['C', 'D'],
             'C' : ['D', 'F'],
             'D' : ['C'],
             'E' : ['F'],
             'F' : ['C'],
             }

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
"""
    Faz a chamada para este mesmo arquivo.
"""
if __name__ == "__main__":
    run()
    print("\n")
