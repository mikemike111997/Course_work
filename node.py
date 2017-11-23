import math


class Node:
    def __str__(self):
        txt = 'Node #{} of network #{} is_satellite = {}\n'.format(self.id, self.network_id, self.is_satellite)
        txt += '\thas {} connected nodes\n'.format(len(self.routing_table))
        return txt

    def __init__(self, _id, network_id, x, y, is_satellite=False):
        self.id = _id
        self.network_id = network_id
        self.is_satellite = is_satellite
        self.routing_table = {}
        self.x = x
        self.y = y


if __name__ == '__main__':
    nodes = [Node(i, 0) for i in range(10)]
    nodes[0].routing_table[1] = 3
    nodes[0].routing_table[2] = 3
    print(nodes[0])