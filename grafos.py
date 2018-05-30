#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    Grafos é uma classe que ira gerenciar as sugestões e as suas dependencias,
definindo assim qual será a melhor sugestão ou a pior, tendo como base os
critérios de pontuação e necessidade de assunto prévio.
"""
class Grafos(object):
    def __init__(self):
        self.sugs={}

    def add_sugestao(self, Sugestao):
        sug = Sugestao
        self.sugs[sug.id] = []
        if sug.dependencias != None:
            for s in range(len(sug.dependencias)):
                print("s is %s, id %d" %(sug.dependencias[s].autor, sug.dependencias[s].id))
                self.sugs[sug.id].append(sug.dependencias[s].id)

    def find_path(self, graph, start, end, path=[]):
        path = path + [start]
        if start == end:
            return path
        if not start in graph:
            return None
        for node in graph[start]:
            if node not in path:
                new_path = self.find_path(graph, node, end, path)
                if new_path: return new_path
        return None

    def find_all_paths(self, graph, start, end, path=[]):
        path = path +[start]
        if start == end:
            return [path]
        if not start in graph:
            return []
        paths = []
        for node in graph[start]:
            if node not in path:
                new_paths = self.find_all_paths(graph, node, end, path)
                for new_path in new_paths:
                    paths.append(new_path)
        return paths

    def find_shortest_path(self, graph, start, end, path=[]):
        path = path + [start]
        if start == end:
            return path
        if start not in graph:
            return None
        shortest = None
        for node in graph[start]:
            if node not in path:
                new_path = self.find_shortest_path(graph, node, end, path)
                if new_path:
                    if not shortest or len(new_path) < len(shortest):
                        shortest = new_path
        return shortest