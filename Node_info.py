from ui.node_info import Ui_Dialog
import sys

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *

class NodeInfo(Ui_Dialog):
    def __init__(self, parent = None, node_name=0, data=None):
        super().__init__(parent)
        self.setupUi(self)
        self.lbl_node_number.setText('Node # {}'.format(str(node_name)))
        if data:
            self.textBrowser.setText(str(data))

if __name__ == '__main__':
    try:
        app = QApplication(sys.argv)
        mySW = NodeInfo()
        mySW.show()
        sys.exit(app.exec_())
    except Exception as err:
        print(err)