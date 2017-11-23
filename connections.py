from node import Node
from global_data import *
import numpy as np

class Connections:
    def __str__(self):
        txt = 'CONNECTIONS ARRAY\n'
        for wan in range(NUMBER_OF_WANS):
            wan_size = TOTAL_NODES[wan]
            txt += 'WAN{} description\n'.format(wan)
            for i in range(wan_size):
                for j in range(wan_size):
                    txt += " " + str(self.connections[wan][i][j])
                txt += '\n'
        return txt

    def __init__(self):
        self.connections = []
        self.connect_types = []
        for i in range(NUMBER_OF_WANS):
            self.connections.append(np.zeros(shape=(TOTAL_NODES[i], TOTAL_NODES[i]), dtype=np.int32))
            self.connect_types.append(np.ndarray(shape=(TOTAL_NODES[i], TOTAL_NODES[i]), dtype=str))
        self.nodes = {}

    def add_node(self, _id, network_id, x, y, is_satellite=False):
        self.nodes[_id] = Node(_id, network_id, x, y, is_satellite)


    # def add_connection(self, left_node, right_node, weight, _type):

if __name__ == '__main__':
    c = Connections()
    print(c)