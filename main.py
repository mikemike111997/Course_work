from settings import *
from graph import *
from global_data import *
from connections import Connections
from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtGui import QPainter, QColor, QPen
from PyQt5.QtCore import Qt
import sys, random, math
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
        self.connection = Connections()
        self.visualize_()
        self.connections()

    def visualize_(self):
        color = [QtCore.Qt.red, QtCore.Qt.green, QtCore.Qt.blue]
        x_centroid = (self.graphicsView.width()/3)
        y_centroid = (self.graphicsView.height()/2)
        self.history = {}
        for area in range(NUMBER_OF_WANS):
            x = x_centroid * area + (x_centroid/2)
            print('XXXX = {}'.format(x))
            print('YYYY = {}'.format(y_centroid))
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
                self.connection.add_node(_id, area, X, y)
                print('Area = {} \t X = {} \t Y = {} \tangle = {} \t_id = {}'.format(area, X, y, angle, _id))
                # self.history[_id] = \
                self.scene.addEllipse(X, y, 10, 10, pen, brush)
                self.scene.addText(str(_id)).setPos(X, y-30)

    def connections(self):
        try:
            self.graphicsView.mousePressEvent = lambda event: self.left_node(event)
        except Exception as err:
            print(err)

    def left_node(self, event):
        print('EVENT = {}'.format(event))
        X = event.x()
        Y = event.y()
        print('\tglobal X = {} \tglobal Y = {}'.format(X, Y))
        print(self.graphicsView.itemAt(X, Y))

if __name__ == '__main__':
    try:
        app = QApplication(sys.argv)
        mySW = Draw()
        mySW.show()
        sys.exit(app.exec_())
    except Exception as err:
        print(err)