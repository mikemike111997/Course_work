import numpy as np

from Node.global_data import *
from Node.node import Node


class Connections:
    def __str__(self):
        txt = 'CONNECTIONS ARRAY\n'
        tmp = 'CONNECTIONS TYPE ARRAY\n'
        for i in range(self.t_nodes):
            for j in range(self.t_nodes):
                txt += " " + str(self.connections[i][j])
                tmp += " " + str(self.connect_types[i][j])
            txt += '\n'
            tmp += '\n'
        return txt+tmp

    def __init__(self, nodes):
        self.nodes = nodes
        self.t_nodes = sum(TOTAL_NODES)
        self.connections = (np.zeros(shape=(self.t_nodes, self.t_nodes), dtype=np.int32))
        self.connect_types = (np.zeros(shape=(self.t_nodes, self.t_nodes), dtype=np.int8))


    def add_connection(self, left_node, right_node, weight, _type=0):
        self.nodes[left_node].add_way(right_node, weight, _type)
        self.connections[left_node][right_node] = weight
        self.connect_types[left_node][right_node] = _type

        self.nodes[right_node].add_way(left_node, weight, _type)
        self.connections[right_node][left_node] = weight
        self.connect_types[right_node][left_node] = _type


    def delete_connection(self, left_node, right_node):
        try:
            self.nodes[left_node].delete_way(right_node)
            self.connections[left_node][right_node] = 0

            self.nodes[right_node].delete_way(left_node)
            self.connections[right_node][left_node] = 0
        except Exception as err:
            print('connections.py -> delete_connection {}'.format(err))

    def connection_exists(self, left_node, right_node):
        return self.connections[left_node][right_node] != 0

if __name__ == '__main__':
    nodes = [Node(i, 0, 0, 0) for i in range(sum(TOTAL_NODES))]
    c = Connections(nodes)
    c.add_connection(0, 4, 10)
    print(c)