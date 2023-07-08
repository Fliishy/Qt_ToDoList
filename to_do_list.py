# Import the PySide modules
import sys
from PySide6 import QtCore, QtGui
from PySide6.QtCore import Qt
from PySide6.QtWidgets import *

# import the UI created in designer (see UI folder)
from UI.to_do_ui import Ui_to_do

class ToDo(QWidget, Ui_to_do):

    def __init__(self):
        super().__init__()
        # sets up the UI
        self.setupUi(self)

        # when the pushbutton called Add Item is clicked it calls the add_list_element slot
        self.pb_add_item.clicked.connect(self.add_list_element)
        # when the pushbutton called Delete Item is clicked it calls the delete_list_element slot
        self.pb_delete_item.clicked.connect(self.delete_list_element)
        # when the pushbutton Delete All is clicked it calls the clear_all slot
        self.pb_delete_all.clicked.connect(self.clear_all)

        # creates the strikeout font when called
        self.strikeout_font = self.create_strikeout_font()
        # retrieves the default font when called
        self.default_font = self.list_widget.font()

        # checks to see if the listwidget has been changed and runs the item_checked if it has
        self.list_widget.itemChanged.connect(self.item_checked)

    # creates the strikeout font
    def create_strikeout_font(self):
        font = self.list_widget.font()
        font.setStrikeOut(True)
        return font
    
    # checks to see if the item is checked and applies a strikeout + color change if it is/isn
    def item_checked(self, item):
        if item.checkState() == Qt.Checked:
            item.setFont(self.strikeout_font)
            item.setForeground(QtGui.QColor(90, 90, 90, 60))
        else:
            item.setFont(self.default_font)
            item.setForeground(QtGui.QColor(0, 0, 0, 255))

    # defines the slot called add_item
    @QtCore.Slot()
    def add_list_element(self):
        # creates an list widget item that defaults to underscores    
        self.item = QListWidgetItem('_________________')
        # sets the item as editable so a user can input their own text
        self.item.setFlags(self.item.flags() | Qt.ItemIsEditable)
        # sets the item as checkable so the user can check a box
        # the box default is unchecked
        self.item.setFlags(self.item.flags() | Qt.ItemIsUserCheckable)
        self.item.setCheckState(QtCore.Qt.Unchecked)
        # when the Add Button is pressed it adds an editable item to the list widget
        self.list_widget.addItem(self.item)

    @QtCore.Slot()
    def delete_list_element(self):
        # deletes the currently selected list item when the Delete Item button is pressed
        self.list_widget.takeItem(self.list_widget.currentRow())

    @QtCore.Slot()
    def clear_all(self):
        # deletes all items in the list widget
        self.list_widget.clear()


# creates an instance of QApplication and executes the program
if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = ToDo()
    window.show()

    # window.check_item_state()

    # terminates the program if it is exited
    sys.exit(app.exec())