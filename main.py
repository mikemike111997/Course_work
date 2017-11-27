import math, random
import sys

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *

from Node.connections import Connections
from Node.global_data import *
from Node.node import Node

from ui.graph import *
from ui.settings import *
from New_node_settings import *
from Node_info import *
# QtWidgets.QDialog




class Dialog(Ui_Dialo_creater):
    def __init__(self):
        super().__init__()
        self.setupUi(self)


# QtWidgets.QMainWindow
class Draw(Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.scene = QtWidgets.QGraphicsScene()
        self.graphicsView.setScene(self.scene)

        self.nodes_dict = {}

        self.visualize_()
        self.connections()
        self.left = None
        self.right = None
        self.line = None
        self.history = []
        self.released = None

    def visualize_(self):
        nodes = []
        color = [QtCore.Qt.red, QtCore.Qt.green, QtCore.Qt.blue]
        x_centroid = (self.graphicsView.width()/3)
        y_centroid = (self.graphicsView.height()/2)
        for area in range(NUMBER_OF_WANS):
            x = x_centroid * area + (x_centroid/2)
            # print('XXXX = {}'.format(x))
            # print('YYYY = {}'.format(y_centroid))
            pen = QtGui.QPen(color[area])
            brush = QtGui.QBrush(color[area])

            for i in range(TOTAL_NODES[area]):
                radius = 133
                _id = (i + (TOTAL_NODES[area]*area))
                angle = (_id - TOTAL_NODES[area]* area) \
                        * int(360 / TOTAL_NODES[area])
                # Some hardcoded values

                X = int(x + radius * math.sin(math.radians(angle)))
                y = int(y_centroid + radius * math.cos(math.radians(angle)))
                nodes.append(Node(_id, area, X, y))
                # print('Area = {} \t X = {} \t Y = {} \tangle = {} \t_id = {}'.format(area, X, y, angle, _id))

                tmp_node = QGraphicsEllipseItem(X, y, 10, 10)
                tmp_node.setPen(pen)
                tmp_node.setBrush(brush)

                self.scene.addItem(tmp_node)
                self.nodes_dict[tmp_node] = _id
                self.scene.addText(str(_id)).setPos(X, y-30)

        self.Connections = Connections(nodes)

    def connections(self):
        try:
            self.graphicsView.mousePressEvent = lambda event: self.connect_nodes(event)
        except Exception as err:
            print('ERR = {}'.format(err))

    def connect_nodes(self, event):
        X = event.x()
        Y = event.y()
        item = self.graphicsView.itemAt(X, Y)

        if isinstance(item,  QtWidgets.QGraphicsEllipseItem):
            if not self.left:
                self.left = item
            elif self.left is not item:
                self.right = item

                # input settings of NEW CONNECTION
                self.left_node_id = self.nodes_dict[self.left]
                self.right_node_id = self.nodes_dict[self.right]
                if not self.Connections.connection_exists(self.left_node_id, self.right_node_id):
                    self.dl = NewConnection(self, self.left_node_id, self.right_node_id)
                    # dl.show()
                    self.dl.accepted.connect(self.draw_line)

                    self.dl.exec_()

                self.left = None
                self.right = None
                self.line = None

            else:
                node = self.nodes_dict[item]
                data = self.Connections.nodes[node]
                dl = NodeInfo(self, node, data)
                dl.exec_()
                self.left = None

        elif isinstance(item,  QtWidgets.QGraphicsLineItem):
            self.line = item
            print('Line = {}'.format(self.line))
        else:
            self.line = None

    def draw_line(self):
        x1, y1, w1, h1 = self.left.rect().getRect()
        x2, y2, w2, h2 = self.right.rect().getRect()

        pen = QtGui.QPen(QtCore.Qt.black)
        pen.setWidth(3)
        line = QGraphicsLineItem(x1 + (w1 / 2), y1 + (h1 / 2), x2 + (w2 / 2), y2 + (h2 / 2))
        line.setPen(pen)
        line.setZValue(-1)

        if hasattr(self, 'self.dl'):
            self.tmp_width = self.dl.spinBox_weight.value()
            self.tmp_type = str(self.dl.comboBox_connect_type.currentText())

            self.tmp_type = 0 if self.tmp_type == 'Duplex' else 1
            self.Connections.add_connection(self.left_node_id, self.right_node_id,self.tmp_width, self.tmp_type)
        else:
            self.Connections.add_connection(self.left_node_id, self.right_node_id, random.randint(1, 50),
                                            random.randint(0, 1))

        self.history.append({line: [self.left_node_id, self.right_node_id]})
        # self.scene.addLine(x1+(w1/2), y1+(h1/2), x2+(w2/2), y2+(h2/2), pen)
        self.scene.addItem(line)

        self.left.setZValue(1)
        self.right.setZValue(1)


    def keyPressEvent(self, e):
        if e.key() == Qt.Key_Delete and self.line:
            tmp = [elem for elem in self.history if elem.get(self.line)][0]
            self.Connections.delete_connection(tmp[self.line][0], tmp[self.line][1])
            self.history.remove(tmp)
            self.scene.removeItem(self.line)
            self.scene.update()
            self.line = None

        elif (e.key() == Qt.ControlModifier):
            print('CTR')
        elif (e.key() == Qt.Key_Z and (not self.released)):
            if len(self.history) > 0:
                tmp = self.history.pop()
                line = list(tmp.keys())[0]
                self.Connections.delete_connection(tmp[line][0], tmp[line][1])
                self.scene.removeItem(line)
                self.scene.update()

    def keyReleaseEvent(self, e):
        self.released = True if e.key() == Qt.ControlModifier else False

    def generate_random(self):
        for node in self.nodes_dict:
            self.left = node
            self.left_node_id = self.nodes_dict[node]
            left_node = self.Connections.nodes[self.left_node_id]
            # search node to connect
            time_out = sum(TOTAL_NODES)
            while len(left_node) < 3 and time_out > 0:
                next_node = random.randint(left_node.network_id*TOTAL_NODES[left_node.network_id],
                                           left_node.network_id*TOTAL_NODES[left_node.network_id] +
                                           TOTAL_NODES[left_node.network_id] -1 )
                print(next_node)
                time_out -= 1
                if len(self.Connections.nodes[next_node]) > 2: continue
                self.right_node_id = next_node
                self.right = [elem for elem in self.nodes_dict.keys() if self.nodes_dict[elem] == next_node][0]
                self.draw_line()




if __name__ == '__main__':
    try:
        app = QApplication(sys.argv)
        mySW = Draw()
        mySW.generate_random()
        mySW.show()
        sys.exit(app.exec_())
    except Exception as err:
        print(err)