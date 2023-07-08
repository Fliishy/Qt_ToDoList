# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'to_do.ui'
##
## Created by: Qt User Interface Compiler version 6.5.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QListWidget, QListWidgetItem,
    QPushButton, QSizePolicy, QSpacerItem, QWidget)
import icons_rc

class Ui_to_do(object):
    def setupUi(self, to_do):
        if not to_do.objectName():
            to_do.setObjectName(u"to_do")
        to_do.resize(400, 300)
        font = QFont()
        font.setPointSize(12)
        to_do.setFont(font)
        icon = QIcon()
        icon.addFile(u":/Logo/toDo.png", QSize(), QIcon.Normal, QIcon.Off)
        to_do.setWindowIcon(icon)
        to_do.setToolTipDuration(1)
        self.gridLayout = QGridLayout(to_do)
        self.gridLayout.setObjectName(u"gridLayout")
        self.pb_delete_all = QPushButton(to_do)
        self.pb_delete_all.setObjectName(u"pb_delete_all")
        icon1 = QIcon()
        icon1.addFile(u":/Buttons/remove.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pb_delete_all.setIcon(icon1)

        self.gridLayout.addWidget(self.pb_delete_all, 1, 3, 1, 1)

        self.list_widget = QListWidget(to_do)
        self.list_widget.setObjectName(u"list_widget")

        self.gridLayout.addWidget(self.list_widget, 0, 0, 1, 4)

        self.pb_delete_item = QPushButton(to_do)
        self.pb_delete_item.setObjectName(u"pb_delete_item")

        self.gridLayout.addWidget(self.pb_delete_item, 1, 1, 1, 1)

        self.pb_add_item = QPushButton(to_do)
        self.pb_add_item.setObjectName(u"pb_add_item")
        self.pb_add_item.setMaximumSize(QSize(16777215, 16777215))

        self.gridLayout.addWidget(self.pb_add_item, 1, 0, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 1, 2, 1, 1)


        self.retranslateUi(to_do)

        QMetaObject.connectSlotsByName(to_do)
    # setupUi

    def retranslateUi(self, to_do):
        to_do.setWindowTitle(QCoreApplication.translate("to_do", u"To Do List", None))
        self.pb_delete_all.setText(QCoreApplication.translate("to_do", u"Delete All", None))
        self.pb_delete_item.setText(QCoreApplication.translate("to_do", u"Delete Item", None))
        self.pb_add_item.setText(QCoreApplication.translate("to_do", u"Add Item", None))
    # retranslateUi

