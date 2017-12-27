import math


class Node:
    def __str__(self):
        setll = 'satellite' if self.is_satellite == True else 'not satellite'
        txt = '0 - duplex\n1 - half-duplex\n\n'
        txt += 'Node  of network #{} \nis_satellite = {}\n'.format(self.network_id, setll)
        txt += 'has {} connected nodes\n'.format(len(self.routing_table))
        # txt += '{}'.format(self.routing_table)
        for i in sorted(self.routing_table.keys()):
            txt += '\tNode #{}\tweight = {}\tconnection type = {}\n'.format(i, self.routing_table[i]['weight'],
                                                                          self.routing_table[i]['type'])
        return txt

    def __init__(self, _id, network_id, x, y, is_satellite=False):
        self.id = _id
        self.network_id = network_id
        self.is_satellite = bool(is_satellite)
        self.routing_table = {}
        self.x = x
        self.y = y

    def __len__(self):
        return len(self.routing_table)

    def add_way(self, node, weight, _t=0):
        self.routing_table[node] = {'weight' : weight, 'type' : _t}

    def delete_way(self, node):
        try:
            self.routing_table.pop(node)
        except Exception as err:
            print('node.py -> delete way {}'.format(err))

    def get_info(self):
        return self.routing_table

if __name__ == '__main__':
    nodes = [Node(i, 0, 0, 0) for i in range(10)]
    nodes[0].add_way(3, 10)
    print((nodes[0]))
    print(len(nodes[0]))
    print((nodes[0].get_info()[3]))