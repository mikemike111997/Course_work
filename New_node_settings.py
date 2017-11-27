from ui.new_node import Ui_Dialog_new_connect
import sys

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *


class NewConnection(Ui_Dialog_new_connect):
    def __init__(self, parent = None, left=0, right=1):
        super().__init__(parent)
        self.setupUi(self)
        self.lbl_node1.setText(str(left))
        self.lbl_node2.setText(str(right))
        # self.show()




if __name__ == '__main__':
    try:
        app = QApplication(sys.argv)
        mySW = NewConnection()
        mySW.show()
        sys.exit(app.exec_())
    except Exception as err:
        print(err)