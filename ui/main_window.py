# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainWindowjbuYVg.ui'
##
## Created by: Qt User Interface Compiler version 6.9.1
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
from PySide6.QtWidgets import (QApplication, QComboBox, QGridLayout, QHBoxLayout,
    QLabel, QPlainTextEdit, QPushButton, QSizePolicy,
    QTabWidget, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(1261, 830)
        self.tabWidget = QTabWidget(Form)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setGeometry(QRect(0, 0, 1261, 831))
        self.tab_1 = QWidget()
        self.tab_1.setObjectName(u"tab_1")
        self.gridLayoutWidget = QWidget(self.tab_1)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(10, 10, 1231, 151))
        self.gridLayout_2 = QGridLayout(self.gridLayoutWidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.tab1_Division_label = QLabel(self.gridLayoutWidget)
        self.tab1_Division_label.setObjectName(u"tab1_Division_label")
        font = QFont()
        font.setPointSize(12)
        self.tab1_Division_label.setFont(font)

        self.gridLayout_2.addWidget(self.tab1_Division_label, 1, 5, 1, 1)

        self.tab1_Manager_edit = QPlainTextEdit(self.gridLayoutWidget)
        self.tab1_Manager_edit.setObjectName(u"tab1_Manager_edit")
        self.tab1_Manager_edit.setFont(font)

        self.gridLayout_2.addWidget(self.tab1_Manager_edit, 3, 4, 1, 1)

        self.tab1_Quantity_label = QLabel(self.gridLayoutWidget)
        self.tab1_Quantity_label.setObjectName(u"tab1_Quantity_label")
        self.tab1_Quantity_label.setFont(font)

        self.gridLayout_2.addWidget(self.tab1_Quantity_label, 2, 3, 1, 1)

        self.tab1_Date_label = QLabel(self.gridLayoutWidget)
        self.tab1_Date_label.setObjectName(u"tab1_Date_label")
        self.tab1_Date_label.setFont(font)

        self.gridLayout_2.addWidget(self.tab1_Date_label, 1, 3, 1, 1)

        self.tab1_Date_edit = QPlainTextEdit(self.gridLayoutWidget)
        self.tab1_Date_edit.setObjectName(u"tab1_Date_edit")
        self.tab1_Date_edit.setFont(font)

        self.gridLayout_2.addWidget(self.tab1_Date_edit, 1, 4, 1, 1)

        self.tab1_Manager_label = QLabel(self.gridLayoutWidget)
        self.tab1_Manager_label.setObjectName(u"tab1_Manager_label")
        self.tab1_Manager_label.setFont(font)

        self.gridLayout_2.addWidget(self.tab1_Manager_label, 3, 3, 1, 1)

        self.label_31 = QLabel(self.gridLayoutWidget)
        self.label_31.setObjectName(u"label_31")
        self.label_31.setFont(font)

        self.gridLayout_2.addWidget(self.label_31, 1, 9, 1, 1)

        self.tab1_Contact_edit = QPlainTextEdit(self.gridLayoutWidget)
        self.tab1_Contact_edit.setObjectName(u"tab1_Contact_edit")
        self.tab1_Contact_edit.setFont(font)

        self.gridLayout_2.addWidget(self.tab1_Contact_edit, 3, 6, 1, 1)

        self.tab1_Quantity_edit = QPlainTextEdit(self.gridLayoutWidget)
        self.tab1_Quantity_edit.setObjectName(u"tab1_Quantity_edit")
        self.tab1_Quantity_edit.setFont(font)

        self.gridLayout_2.addWidget(self.tab1_Quantity_edit, 2, 4, 1, 1)

        self.tab1_totalPrice_edit = QPlainTextEdit(self.gridLayoutWidget)
        self.tab1_totalPrice_edit.setObjectName(u"tab1_totalPrice_edit")
        self.tab1_totalPrice_edit.setFont(font)

        self.gridLayout_2.addWidget(self.tab1_totalPrice_edit, 2, 6, 1, 1)

        self.plainTextEdit_25 = QPlainTextEdit(self.gridLayoutWidget)
        self.plainTextEdit_25.setObjectName(u"plainTextEdit_25")
        self.plainTextEdit_25.setFont(font)

        self.gridLayout_2.addWidget(self.plainTextEdit_25, 1, 10, 1, 1)

        self.tab1_Note_label = QLabel(self.gridLayoutWidget)
        self.tab1_Note_label.setObjectName(u"tab1_Note_label")
        self.tab1_Note_label.setFont(font)

        self.gridLayout_2.addWidget(self.tab1_Note_label, 4, 0, 1, 1)

        self.label_29 = QLabel(self.gridLayoutWidget)
        self.label_29.setObjectName(u"label_29")
        self.label_29.setFont(font)

        self.gridLayout_2.addWidget(self.label_29, 1, 7, 1, 1)

        self.tab1_Division_combo = QComboBox(self.gridLayoutWidget)
        self.tab1_Division_combo.setObjectName(u"tab1_Division_combo")

        self.gridLayout_2.addWidget(self.tab1_Division_combo, 1, 6, 1, 1)

        self.label_27 = QLabel(self.gridLayoutWidget)
        self.label_27.setObjectName(u"label_27")
        self.label_27.setFont(font)

        self.gridLayout_2.addWidget(self.label_27, 1, 11, 1, 1)

        self.tab1_Source_label = QLabel(self.gridLayoutWidget)
        self.tab1_Source_label.setObjectName(u"tab1_Source_label")
        self.tab1_Source_label.setFont(font)

        self.gridLayout_2.addWidget(self.tab1_Source_label, 3, 0, 1, 1)

        self.tab1_unitPrice_edit = QPlainTextEdit(self.gridLayoutWidget)
        self.tab1_unitPrice_edit.setObjectName(u"tab1_unitPrice_edit")
        self.tab1_unitPrice_edit.setFont(font)

        self.gridLayout_2.addWidget(self.tab1_unitPrice_edit, 2, 1, 1, 1)

        self.tab1_ID_label = QLabel(self.gridLayoutWidget)
        self.tab1_ID_label.setObjectName(u"tab1_ID_label")
        self.tab1_ID_label.setFont(font)

        self.gridLayout_2.addWidget(self.tab1_ID_label, 1, 0, 1, 1)

        self.tab1_Contact_label = QLabel(self.gridLayoutWidget)
        self.tab1_Contact_label.setObjectName(u"tab1_Contact_label")
        self.tab1_Contact_label.setFont(font)

        self.gridLayout_2.addWidget(self.tab1_Contact_label, 3, 5, 1, 1)

        self.tab1_Note_edit = QPlainTextEdit(self.gridLayoutWidget)
        self.tab1_Note_edit.setObjectName(u"tab1_Note_edit")
        self.tab1_Note_edit.setFont(font)

        self.gridLayout_2.addWidget(self.tab1_Note_edit, 4, 1, 1, 6)

        self.tab1_totalPrice_label = QLabel(self.gridLayoutWidget)
        self.tab1_totalPrice_label.setObjectName(u"tab1_totalPrice_label")
        self.tab1_totalPrice_label.setFont(font)

        self.gridLayout_2.addWidget(self.tab1_totalPrice_label, 2, 5, 1, 1)

        self.plainTextEdit_24 = QPlainTextEdit(self.gridLayoutWidget)
        self.plainTextEdit_24.setObjectName(u"plainTextEdit_24")
        self.plainTextEdit_24.setFont(font)

        self.gridLayout_2.addWidget(self.plainTextEdit_24, 1, 12, 1, 1)

        self.comboBox_5 = QComboBox(self.gridLayoutWidget)
        self.comboBox_5.setObjectName(u"comboBox_5")

        self.gridLayout_2.addWidget(self.comboBox_5, 1, 8, 1, 1)

        self.tab1_unitPrice_label = QLabel(self.gridLayoutWidget)
        self.tab1_unitPrice_label.setObjectName(u"tab1_unitPrice_label")
        self.tab1_unitPrice_label.setFont(font)

        self.gridLayout_2.addWidget(self.tab1_unitPrice_label, 2, 0, 1, 1)

        self.comboBox_10 = QComboBox(self.gridLayoutWidget)
        self.comboBox_10.setObjectName(u"comboBox_10")
        self.comboBox_10.setMinimumSize(QSize(87, 0))
        self.comboBox_10.setMaximumSize(QSize(87, 16777215))

        self.gridLayout_2.addWidget(self.comboBox_10, 2, 2, 1, 1)

        self.tab1_ID_edit = QPlainTextEdit(self.gridLayoutWidget)
        self.tab1_ID_edit.setObjectName(u"tab1_ID_edit")
        self.tab1_ID_edit.setFont(font)

        self.gridLayout_2.addWidget(self.tab1_ID_edit, 1, 1, 1, 2)

        self.tab1_Source_edit = QPlainTextEdit(self.gridLayoutWidget)
        self.tab1_Source_edit.setObjectName(u"tab1_Source_edit")
        self.tab1_Source_edit.setFont(font)

        self.gridLayout_2.addWidget(self.tab1_Source_edit, 3, 1, 1, 2)

        self.horizontalLayoutWidget = QWidget(self.tab_1)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(10, 160, 1231, 31))
        self.horizontalLayout_2 = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.pushButton = QPushButton(self.horizontalLayoutWidget)
        self.pushButton.setObjectName(u"pushButton")

        self.horizontalLayout_2.addWidget(self.pushButton)

        self.pushButton_2 = QPushButton(self.horizontalLayoutWidget)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.horizontalLayout_2.addWidget(self.pushButton_2)

        self.pushButton_3 = QPushButton(self.horizontalLayoutWidget)
        self.pushButton_3.setObjectName(u"pushButton_3")

        self.horizontalLayout_2.addWidget(self.pushButton_3)

        self.pushButton_4 = QPushButton(self.horizontalLayoutWidget)
        self.pushButton_4.setObjectName(u"pushButton_4")

        self.horizontalLayout_2.addWidget(self.pushButton_4)

        self.pushButton_5 = QPushButton(self.horizontalLayoutWidget)
        self.pushButton_5.setObjectName(u"pushButton_5")

        self.horizontalLayout_2.addWidget(self.pushButton_5)

        self.horizontalLayoutWidget_2 = QWidget(self.tab_1)
        self.horizontalLayoutWidget_2.setObjectName(u"horizontalLayoutWidget_2")
        self.horizontalLayoutWidget_2.setGeometry(QRect(10, 190, 1231, 31))
        self.horizontalLayout_3 = QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.comboBox_7 = QComboBox(self.horizontalLayoutWidget_2)
        self.comboBox_7.setObjectName(u"comboBox_7")

        self.horizontalLayout_3.addWidget(self.comboBox_7)

        self.plainTextEdit_11 = QPlainTextEdit(self.horizontalLayoutWidget_2)
        self.plainTextEdit_11.setObjectName(u"plainTextEdit_11")
        self.plainTextEdit_11.setFont(font)

        self.horizontalLayout_3.addWidget(self.plainTextEdit_11)

        self.comboBox_8 = QComboBox(self.horizontalLayoutWidget_2)
        self.comboBox_8.setObjectName(u"comboBox_8")

        self.horizontalLayout_3.addWidget(self.comboBox_8)

        self.plainTextEdit_12 = QPlainTextEdit(self.horizontalLayoutWidget_2)
        self.plainTextEdit_12.setObjectName(u"plainTextEdit_12")
        self.plainTextEdit_12.setFont(font)

        self.horizontalLayout_3.addWidget(self.plainTextEdit_12)

        self.comboBox_9 = QComboBox(self.horizontalLayoutWidget_2)
        self.comboBox_9.setObjectName(u"comboBox_9")

        self.horizontalLayout_3.addWidget(self.comboBox_9)

        self.plainTextEdit_27 = QPlainTextEdit(self.horizontalLayoutWidget_2)
        self.plainTextEdit_27.setObjectName(u"plainTextEdit_27")
        self.plainTextEdit_27.setFont(font)

        self.horizontalLayout_3.addWidget(self.plainTextEdit_27)

        self.widget = QWidget(self.tab_1)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(9, 229, 1231, 561))
        self.tabWidget.addTab(self.tab_1, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_4 = QWidget()
        self.tab_4.setObjectName(u"tab_4")
        self.tabWidget.addTab(self.tab_4, "")
        self.tab_5 = QWidget()
        self.tab_5.setObjectName(u"tab_5")
        self.tabWidget.addTab(self.tab_5, "")

        self.retranslateUi(Form)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.tab1_Division_label.setText(QCoreApplication.translate("Form", u"\uad6c\ubd84", None))
        self.tab1_Quantity_label.setText(QCoreApplication.translate("Form", u"\uc218\ub7c9", None))
        self.tab1_Date_label.setText(QCoreApplication.translate("Form", u"\ub0a0\uc9dc", None))
        self.tab1_Manager_label.setText(QCoreApplication.translate("Form", u"\ub2f4\ub2f9\uc790", None))
        self.label_31.setText(QCoreApplication.translate("Form", u"\ud488\ubaa9\ucf54\ub4dc", None))
        self.tab1_Note_label.setText(QCoreApplication.translate("Form", u"\ube44\uace0", None))
        self.label_29.setText(QCoreApplication.translate("Form", u"\ud488\ubaa9\uad70", None))
        self.label_27.setText(QCoreApplication.translate("Form", u"\ud488\ubaa9\uba85", None))
        self.tab1_Source_label.setText(QCoreApplication.translate("Form", u"\uac70\ub798/\ubd88\ucd9c\ucc98", None))
        self.tab1_ID_label.setText(QCoreApplication.translate("Form", u"ID", None))
        self.tab1_Contact_label.setText(QCoreApplication.translate("Form", u"\uc5f0\ub77d\ucc98", None))
        self.tab1_totalPrice_label.setText(QCoreApplication.translate("Form", u"\uae08\uc561", None))
        self.tab1_unitPrice_label.setText(QCoreApplication.translate("Form", u"\ub2e8\uac00", None))
        self.pushButton.setText(QCoreApplication.translate("Form", u"\uc2e0\uaddc", None))
        self.pushButton_2.setText(QCoreApplication.translate("Form", u"\uc800\uc7a5", None))
        self.pushButton_3.setText(QCoreApplication.translate("Form", u"\ubc14\ucf54\ub4dc \uc5f0\ub3d9(\ub3d9\uae30\ud654)", None))
        self.pushButton_4.setText(QCoreApplication.translate("Form", u"\uc0ad\uc81c", None))
        self.pushButton_5.setText(QCoreApplication.translate("Form", u"\uc5d1\uc140/CSV \ub0b4\ubcf4\ub0b4\uae30", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_1), QCoreApplication.translate("Form", u"\uba54\uc778\uc2dc\ud2b8", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("Form", u"\ud488\ubaa9\ubcc4 \uc138\ubd80\ubcf4\uc720 \ud604\ud669", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QCoreApplication.translate("Form", u"\uae30\uac04\ubcc4 \uc7ac\uace0 \uc870\ud68c", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), QCoreApplication.translate("Form", u"\ud0c0\uac9f\ubcf4\uc720 \ud604\ud669", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), QCoreApplication.translate("Form", u"\ubc14\ucf54\ub4dc", None))
    # retranslateUi

