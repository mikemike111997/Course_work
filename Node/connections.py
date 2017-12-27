import numpy as np
# class Ui_MainWindow(QtWidgets.QMainWindow):

if __name__ == '__main__':
    from global_data import *
    from node import Node
else:
    from Node.global_data import *
    from Node.node import Node


class Connections:
    def __str__(self):
        txt = 'CONNECTIONS ARRAY\n'
        txt += " " + str(self.connections)
        txt += '\n'
        return txt

    def __init__(self, nodes):
        self.nodes = nodes
        self.t_nodes = sum(TOTAL_NODES)
        self.connections = {}
        # self.connect_types = (np.zeros(shape=(self.t_nodes, self.t_nodes), dtype=np.int8))


    def add_connection(self, left_node, right_node, weight, _type=0):
        self.nodes[left_node].add_way(right_node, weight, _type)
        self.connections[left_node] = self.nodes[left_node].get_info()
        # self.connect_types[left_node] =

        self.nodes[right_node].add_way(left_node, weight, _type)
        self.connections[right_node] = self.nodes[right_node].get_info()
        # self.connect_types[right_node][left_node] = _type


    def delete_connection(self, left_node, right_node):
        try:
            self.nodes[left_node].delete_way(right_node)
            self.connections[left_node][right_node] = 0

            self.nodes[right_node].delete_way(left_node)
            self.connections[right_node][left_node] = 0
        except Exception as err:
            print('connections.py -> delete_connection {}'.format(err))

    def connection_exists(self, left_node, right_node):
        return right_node in list(self.connections[left_node].keys())

    # def dijkstra(self, src, dest, visited=[], distances={}, predecessors={}):
    #     """ calculates a shortest path tree routed in src
    #     """
    #     # a few sanity checks
    #     # if src not in graph:
    #     #     raise TypeError('The root of the shortest path tree cannot be found')
    #     # if dest not in graph:
    #     #     raise TypeError('The target of the shortest path cannot be found')
    #     #     # ending condition
    #     print('src = {} dst = {}\n{}\n'.format(src, dest, self.connections[src]))
    #     if src == dest:
    #         path = list()
    #         # We build the shortest path and display it
    #         # path = []
    #         pred = dest
    #         while pred != None:
    #             path.append(pred)
    #             # distances[dest] = 0
    #             pred = predecessors.get(pred, None)
    #         print('shortest path: ' + str(path) + " cost=" + str(distances[dest]))
    #         # self.path = path.copy()
    #
    #     else:
    #         # if it is the initial  run, initializes the cost
    #         if not visited:
    #             distances[src] = 0
    #         # visit the neighbors
    #         for neighbor in self.connections[src]:
    #             print('\tneighbor = {}'.format(neighbor))
    #             if neighbor not in visited:
    #                 new_distance = distances[src] + self.connections[src][neighbor]['weight']
    #                 if new_distance < distances.get(neighbor, float('inf')):
    #                     distances[neighbor] = new_distance
    #                     predecessors[neighbor] = src
    #         # mark as visited
    #         visited.append(src)
    #         # now that all neighbors have been visited: recurse
    #         # select the non visited node with lowest distance 'x'
    #         # run Dijskstra with src='x'
    #         unvisited = {}
    #         for k in self.connections:
    #             if k not in visited:
    #                 unvisited[k] = distances.get(k, float('inf'))
    #         if len(unvisited) > 0:
    #             x = min(unvisited, key=unvisited.get)
    #             self.dijkstra(x, dest, visited, distances, predecessors)
    #         else:
    #             # return path
    #             pass
    #     return path

    def dijkstra(self, src, dst):
        # empty dictionary to hold distances
        # print(self.connections)
        distances = {}
        # list of vertices in path to current vertex
        predecessors = {}

        # get all the nodes that need to be assessed
        to_assess = self.connections.keys()

        # set all initial distances to infinity
        #  and no predecessor for any node
        for node in self.connections:
            # print(node)
            distances[node] = float('inf')
            predecessors[node] = None

        # set the initial collection of
        # permanently labelled nodes to be empty
        sp_set = []

        # set the distance from the start node to be 0
        distances[src] = 0

        # as long as there are still nodes to assess:
        while len(sp_set) < len(to_assess):

            # chop out any nodes with a permanent label
            still_in = {node: distances[node] \
                        for node in [node for node in \
                                     to_assess if node not in sp_set]}

            # find the closest node to the current node
            closest = min(still_in, key=distances.get)

            # and add it to the permanently labelled nodes
            sp_set.append(closest)

            # then for all the neighbours of
            # the closest node (that was just added to
            # the permanent set)
            for node in self.connections[closest]:
                # if a shorter path to that node can be found
                if distances[node] > distances[closest] + \
                        self.connections[closest][node]['weight']:
                    # update the distance with
                    # that shorter distance
                    distances[node] = distances[closest] + \
                                      self.connections[closest][node]['weight']

                    # set the predecessor for that node
                    predecessors[node] = closest

        # once the loop is complete the final
        # path needs to be calculated - this can
        # be done by backtracking through the predecessors
        path = [dst]
        while src not in path:
            path.append(predecessors[path[-1]])

        # return the path in order start -> end, and it's cost
        return path[::-1], distances[dst]

    def send_data(self, src, dst, msg, package_size=64, servise_size =4, _type = 'virtual'):
        path, dist = self.dijkstra(src, dst)
        if len(path) == 0:
            return 'No way!'
        if _type == 'virtual':
            msg_size = len(msg)*8
            packages = int(msg_size / (package_size - servise_size)) + 1
            txt = 'PATH {}\n'.format(path)
            print(path)
            p = ''
            t_time = 0
            for i in range(len(path) - 1):
                # print(self.nodes[path[i+1]].routing_table)
                type_of_connect = self.nodes[path[i]].routing_table[path[i+1]]['type'] + 1
                time = (self.nodes[path[i]].routing_table[path[i + 1]]['weight'] * type_of_connect) * (packages * 2 + 2)
                if not self.nodes[i].is_satellite:
                    time *= 3
                t_time +=time
                p += '{} -> time: {}\tpackages: {}\tservice_packages: {}\n'.format(path[i+1], time, packages*2+2,
                                                                                   packages+2)
                print(p)
            txt += p
            txt += ('msg_size = {}\tservice_data_size = {}\n\tt_time = {}'.format(msg_size, (packages*2+2) * servise_size,
                    t_time))
            return txt
        else:
            msg_size = len(msg)*8
            packages = int(msg_size / (package_size - servise_size)) + 1
            txt = 'PATH {}\n'.format(path)
            print(path)
            p = ''
            t_time = 0
            for i in range(len(path) - 1):
                # print(self.nodes[path[i+1]].routing_table)
                type_of_connect = self.nodes[path[i]].routing_table[path[i+1]]['type'] + 1
                time = (self.nodes[path[i]].routing_table[path[i + 1]]['weight'] * type_of_connect) * (packages + 2)
                t_time += time
                if not self.nodes[i].is_satellite:
                    time *= 3

                p += '{} -> time: {}\tpackages: {}\tservice_packages: {}\n'.format(path[i+1], time, packages,
                                                                                   packages+2)
                print(p)
            txt += p
            txt += ('msg_size = {}\tservice_data_size = {}\n\tt_time = {}'.format(msg_size, (packages+2) * servise_size,
                    t_time))
            return txt


if __name__ == '__main__':
    nodes = [Node(i, 0, 0, 0) for i in range(sum(TOTAL_NODES))]
    c = Connections(nodes)
    c.add_connection(0, 4, 10)
    c.add_connection(4, 10, 3)
    c.add_connection(10, 3, 3)
    # print(c)
    c.send_data(0, 3, 'txt11111 sd', _type='virtual')
