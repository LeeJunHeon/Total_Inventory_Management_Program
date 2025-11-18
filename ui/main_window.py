# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainWindowfpqsKo.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QGridLayout,
    QHBoxLayout, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QSpacerItem, QTabWidget, QVBoxLayout,
    QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(1252, 847)
        self.verticalLayout_4 = QVBoxLayout(Form)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.tabWidget = QTabWidget(Form)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tab_5 = QWidget()
        self.tab_5.setObjectName(u"tab_5")
        self.verticalLayout_3 = QVBoxLayout(self.tab_5)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.tab1_manager_lineEdit = QLineEdit(self.tab_5)
        self.tab1_manager_lineEdit.setObjectName(u"tab1_manager_lineEdit")

        self.gridLayout_3.addWidget(self.tab1_manager_lineEdit, 2, 3, 1, 1)

        self.tab1_contact_lineEdit = QLineEdit(self.tab_5)
        self.tab1_contact_lineEdit.setObjectName(u"tab1_contact_lineEdit")

        self.gridLayout_3.addWidget(self.tab1_contact_lineEdit, 2, 5, 1, 1)

        self.tab1_itemCode_lineEdit = QLineEdit(self.tab_5)
        self.tab1_itemCode_lineEdit.setObjectName(u"tab1_itemCode_lineEdit")

        self.gridLayout_3.addWidget(self.tab1_itemCode_lineEdit, 0, 9, 1, 1)

        self.tab1_totalPrice_label = QLabel(self.tab_5)
        self.tab1_totalPrice_label.setObjectName(u"tab1_totalPrice_label")
        font = QFont()
        font.setPointSize(11)
        self.tab1_totalPrice_label.setFont(font)

        self.gridLayout_3.addWidget(self.tab1_totalPrice_label, 1, 4, 1, 1)

        self.tab1_source_label = QLabel(self.tab_5)
        self.tab1_source_label.setObjectName(u"tab1_source_label")
        self.tab1_source_label.setFont(font)

        self.gridLayout_3.addWidget(self.tab1_source_label, 2, 0, 1, 1)

        self.tab1_division_label = QLabel(self.tab_5)
        self.tab1_division_label.setObjectName(u"tab1_division_label")
        self.tab1_division_label.setFont(font)

        self.gridLayout_3.addWidget(self.tab1_division_label, 0, 4, 1, 1)

        self.tab1_itemGroup_comboBox = QComboBox(self.tab_5)
        self.tab1_itemGroup_comboBox.setObjectName(u"tab1_itemGroup_comboBox")

        self.gridLayout_3.addWidget(self.tab1_itemGroup_comboBox, 0, 7, 1, 1)

        self.tab1_date_lineEdit = QLineEdit(self.tab_5)
        self.tab1_date_lineEdit.setObjectName(u"tab1_date_lineEdit")

        self.gridLayout_3.addWidget(self.tab1_date_lineEdit, 0, 3, 1, 1)

        self.tab1_quantity_lineEdit = QLineEdit(self.tab_5)
        self.tab1_quantity_lineEdit.setObjectName(u"tab1_quantity_lineEdit")

        self.gridLayout_3.addWidget(self.tab1_quantity_lineEdit, 1, 3, 1, 1)

        self.tab1_unitPrice_label = QLabel(self.tab_5)
        self.tab1_unitPrice_label.setObjectName(u"tab1_unitPrice_label")
        self.tab1_unitPrice_label.setFont(font)

        self.gridLayout_3.addWidget(self.tab1_unitPrice_label, 1, 0, 1, 1)

        self.tab1_date_label = QLabel(self.tab_5)
        self.tab1_date_label.setObjectName(u"tab1_date_label")
        self.tab1_date_label.setFont(font)

        self.gridLayout_3.addWidget(self.tab1_date_label, 0, 2, 1, 1)

        self.tab1_note_lineEdit = QLineEdit(self.tab_5)
        self.tab1_note_lineEdit.setObjectName(u"tab1_note_lineEdit")

        self.gridLayout_3.addWidget(self.tab1_note_lineEdit, 3, 1, 1, 5)

        self.tab1_unitPrice_lineEdit = QLineEdit(self.tab_5)
        self.tab1_unitPrice_lineEdit.setObjectName(u"tab1_unitPrice_lineEdit")

        self.gridLayout_3.addWidget(self.tab1_unitPrice_lineEdit, 1, 1, 1, 1)

        self.tab1_targetID_label = QLabel(self.tab_5)
        self.tab1_targetID_label.setObjectName(u"tab1_targetID_label")
        font1 = QFont()
        font1.setPointSize(12)
        self.tab1_targetID_label.setFont(font1)

        self.gridLayout_3.addWidget(self.tab1_targetID_label, 3, 6, 1, 1)

        self.tab1_contact_label = QLabel(self.tab_5)
        self.tab1_contact_label.setObjectName(u"tab1_contact_label")
        self.tab1_contact_label.setFont(font)

        self.gridLayout_3.addWidget(self.tab1_contact_label, 2, 4, 1, 1)

        self.tab1_itemName_label = QLabel(self.tab_5)
        self.tab1_itemName_label.setObjectName(u"tab1_itemName_label")
        self.tab1_itemName_label.setFont(font)

        self.gridLayout_3.addWidget(self.tab1_itemName_label, 0, 10, 1, 1)

        self.tab1_itemCode_label = QLabel(self.tab_5)
        self.tab1_itemCode_label.setObjectName(u"tab1_itemCode_label")
        self.tab1_itemCode_label.setFont(font)

        self.gridLayout_3.addWidget(self.tab1_itemCode_label, 0, 8, 1, 1)

        self.tab1_quantity_label = QLabel(self.tab_5)
        self.tab1_quantity_label.setObjectName(u"tab1_quantity_label")
        self.tab1_quantity_label.setFont(font)

        self.gridLayout_3.addWidget(self.tab1_quantity_label, 1, 2, 1, 1)

        self.tab1_note_label = QLabel(self.tab_5)
        self.tab1_note_label.setObjectName(u"tab1_note_label")
        self.tab1_note_label.setFont(font1)

        self.gridLayout_3.addWidget(self.tab1_note_label, 3, 0, 1, 1)

        self.tab1_manager_label = QLabel(self.tab_5)
        self.tab1_manager_label.setObjectName(u"tab1_manager_label")
        self.tab1_manager_label.setFont(font)

        self.gridLayout_3.addWidget(self.tab1_manager_label, 2, 2, 1, 1)

        self.tab1_id_lineEdit = QLineEdit(self.tab_5)
        self.tab1_id_lineEdit.setObjectName(u"tab1_id_lineEdit")

        self.gridLayout_3.addWidget(self.tab1_id_lineEdit, 0, 1, 1, 1)

        self.tab1_division_lineEdit = QLineEdit(self.tab_5)
        self.tab1_division_lineEdit.setObjectName(u"tab1_division_lineEdit")

        self.gridLayout_3.addWidget(self.tab1_division_lineEdit, 0, 5, 1, 1)

        self.tab1_itemGroup_label = QLabel(self.tab_5)
        self.tab1_itemGroup_label.setObjectName(u"tab1_itemGroup_label")
        self.tab1_itemGroup_label.setFont(font)

        self.gridLayout_3.addWidget(self.tab1_itemGroup_label, 0, 6, 1, 1)

        self.tab1_source_lineEdit = QLineEdit(self.tab_5)
        self.tab1_source_lineEdit.setObjectName(u"tab1_source_lineEdit")

        self.gridLayout_3.addWidget(self.tab1_source_lineEdit, 2, 1, 1, 1)

        self.tab1_targetID_lineEdit = QLineEdit(self.tab_5)
        self.tab1_targetID_lineEdit.setObjectName(u"tab1_targetID_lineEdit")

        self.gridLayout_3.addWidget(self.tab1_targetID_lineEdit, 3, 7, 1, 5)

        self.tab1_id_label = QLabel(self.tab_5)
        self.tab1_id_label.setObjectName(u"tab1_id_label")
        self.tab1_id_label.setFont(font)

        self.gridLayout_3.addWidget(self.tab1_id_label, 0, 0, 1, 1)

        self.tab1_itemName_lineEdit = QLineEdit(self.tab_5)
        self.tab1_itemName_lineEdit.setObjectName(u"tab1_itemName_lineEdit")

        self.gridLayout_3.addWidget(self.tab1_itemName_lineEdit, 0, 11, 1, 1)

        self.tab1_totalPrice_lineEdit = QLineEdit(self.tab_5)
        self.tab1_totalPrice_lineEdit.setObjectName(u"tab1_totalPrice_lineEdit")

        self.gridLayout_3.addWidget(self.tab1_totalPrice_lineEdit, 1, 5, 1, 1)


        self.verticalLayout_3.addLayout(self.gridLayout_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.tab1_new_pushButton = QPushButton(self.tab_5)
        self.tab1_new_pushButton.setObjectName(u"tab1_new_pushButton")

        self.horizontalLayout_4.addWidget(self.tab1_new_pushButton)

        self.tab1_save_pushButton = QPushButton(self.tab_5)
        self.tab1_save_pushButton.setObjectName(u"tab1_save_pushButton")

        self.horizontalLayout_4.addWidget(self.tab1_save_pushButton)

        self.tab1_barcodeLink_pushButton = QPushButton(self.tab_5)
        self.tab1_barcodeLink_pushButton.setObjectName(u"tab1_barcodeLink_pushButton")

        self.horizontalLayout_4.addWidget(self.tab1_barcodeLink_pushButton)

        self.tab1_delete_pushButton = QPushButton(self.tab_5)
        self.tab1_delete_pushButton.setObjectName(u"tab1_delete_pushButton")

        self.horizontalLayout_4.addWidget(self.tab1_delete_pushButton)

        self.tab1_exportEcvelCsv_pushButton = QPushButton(self.tab_5)
        self.tab1_exportEcvelCsv_pushButton.setObjectName(u"tab1_exportEcvelCsv_pushButton")

        self.horizontalLayout_4.addWidget(self.tab1_exportEcvelCsv_pushButton)


        self.verticalLayout_3.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.tab1_search1_field_comboBox = QComboBox(self.tab_5)
        self.tab1_search1_field_comboBox.setObjectName(u"tab1_search1_field_comboBox")

        self.horizontalLayout_5.addWidget(self.tab1_search1_field_comboBox)

        self.tab1_search1_text_lineEdit = QLineEdit(self.tab_5)
        self.tab1_search1_text_lineEdit.setObjectName(u"tab1_search1_text_lineEdit")

        self.horizontalLayout_5.addWidget(self.tab1_search1_text_lineEdit)

        self.tab1_search2_field_comboBox = QComboBox(self.tab_5)
        self.tab1_search2_field_comboBox.setObjectName(u"tab1_search2_field_comboBox")

        self.horizontalLayout_5.addWidget(self.tab1_search2_field_comboBox)

        self.tab1_search2_text_lineEdit = QLineEdit(self.tab_5)
        self.tab1_search2_text_lineEdit.setObjectName(u"tab1_search2_text_lineEdit")

        self.horizontalLayout_5.addWidget(self.tab1_search2_text_lineEdit)

        self.tab1_search3_field_comboBox = QComboBox(self.tab_5)
        self.tab1_search3_field_comboBox.setObjectName(u"tab1_search3_field_comboBox")

        self.horizontalLayout_5.addWidget(self.tab1_search3_field_comboBox)

        self.tab1_search3_text_lineEdit = QLineEdit(self.tab_5)
        self.tab1_search3_text_lineEdit.setObjectName(u"tab1_search3_text_lineEdit")

        self.horizontalLayout_5.addWidget(self.tab1_search3_text_lineEdit)


        self.verticalLayout_3.addLayout(self.horizontalLayout_5)

        self.tab1_mainSheet_tableWidget = QWidget(self.tab_5)
        self.tab1_mainSheet_tableWidget.setObjectName(u"tab1_mainSheet_tableWidget")
        self.tab1_mainSheet_tableWidget.setAutoFillBackground(True)

        self.verticalLayout_3.addWidget(self.tab1_mainSheet_tableWidget)

        self.verticalLayout_3.setStretch(3, 5)
        self.tabWidget.addTab(self.tab_5, "")
        self.tab_6 = QWidget()
        self.tab_6.setObjectName(u"tab_6")
        self.horizontalLayout_13 = QHBoxLayout(self.tab_6)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.gridLayout_4 = QGridLayout()
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.frame = QFrame(self.tab_6)
        self.frame.setObjectName(u"frame")
        self.frame.setAutoFillBackground(True)
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.tab2_waferInventory_label = QLabel(self.frame)
        self.tab2_waferInventory_label.setObjectName(u"tab2_waferInventory_label")

        self.horizontalLayout_6.addWidget(self.tab2_waferInventory_label)

        self.tab2_waferRequiredQty_pushButton = QPushButton(self.frame)
        self.tab2_waferRequiredQty_pushButton.setObjectName(u"tab2_waferRequiredQty_pushButton")

        self.horizontalLayout_6.addWidget(self.tab2_waferRequiredQty_pushButton)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer)


        self.verticalLayout_2.addLayout(self.horizontalLayout_6)

        self.tab2_waferSearch_lineEdit = QLineEdit(self.frame)
        self.tab2_waferSearch_lineEdit.setObjectName(u"tab2_waferSearch_lineEdit")

        self.verticalLayout_2.addWidget(self.tab2_waferSearch_lineEdit)

        self.tab2_waferInventory_tableWidget = QWidget(self.frame)
        self.tab2_waferInventory_tableWidget.setObjectName(u"tab2_waferInventory_tableWidget")
        self.tab2_waferInventory_tableWidget.setAutoFillBackground(True)

        self.verticalLayout_2.addWidget(self.tab2_waferInventory_tableWidget)

        self.verticalLayout_2.setStretch(2, 1)

        self.gridLayout_4.addWidget(self.frame, 0, 0, 1, 1)

        self.frame_2 = QFrame(self.tab_6)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setAutoFillBackground(True)
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.frame_2)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.tab2_gasInventory_label = QLabel(self.frame_2)
        self.tab2_gasInventory_label.setObjectName(u"tab2_gasInventory_label")

        self.horizontalLayout_10.addWidget(self.tab2_gasInventory_label)

        self.tab2_gasRequiredQty_pushButton = QPushButton(self.frame_2)
        self.tab2_gasRequiredQty_pushButton.setObjectName(u"tab2_gasRequiredQty_pushButton")

        self.horizontalLayout_10.addWidget(self.tab2_gasRequiredQty_pushButton)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_10.addItem(self.horizontalSpacer_2)


        self.verticalLayout_8.addLayout(self.horizontalLayout_10)

        self.tab2_gasSearch_lineEdit = QLineEdit(self.frame_2)
        self.tab2_gasSearch_lineEdit.setObjectName(u"tab2_gasSearch_lineEdit")

        self.verticalLayout_8.addWidget(self.tab2_gasSearch_lineEdit)

        self.tab2_gasInventory_tableWidget = QWidget(self.frame_2)
        self.tab2_gasInventory_tableWidget.setObjectName(u"tab2_gasInventory_tableWidget")
        self.tab2_gasInventory_tableWidget.setAutoFillBackground(True)

        self.verticalLayout_8.addWidget(self.tab2_gasInventory_tableWidget)

        self.verticalLayout_8.setStretch(2, 1)

        self.gridLayout_4.addWidget(self.frame_2, 1, 0, 1, 1)

        self.frame_3 = QFrame(self.tab_6)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setAutoFillBackground(True)
        self.frame_3.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.frame_3)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.tab2_targetInventory_label = QLabel(self.frame_3)
        self.tab2_targetInventory_label.setObjectName(u"tab2_targetInventory_label")

        self.horizontalLayout_11.addWidget(self.tab2_targetInventory_label)

        self.tab2_targetRequiredQty_pushButton = QPushButton(self.frame_3)
        self.tab2_targetRequiredQty_pushButton.setObjectName(u"tab2_targetRequiredQty_pushButton")

        self.horizontalLayout_11.addWidget(self.tab2_targetRequiredQty_pushButton)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_11.addItem(self.horizontalSpacer_3)


        self.verticalLayout_9.addLayout(self.horizontalLayout_11)

        self.tab2_targetSearch_lineEdit = QLineEdit(self.frame_3)
        self.tab2_targetSearch_lineEdit.setObjectName(u"tab2_targetSearch_lineEdit")

        self.verticalLayout_9.addWidget(self.tab2_targetSearch_lineEdit)

        self.tab2_targetInventory_tableWidget = QWidget(self.frame_3)
        self.tab2_targetInventory_tableWidget.setObjectName(u"tab2_targetInventory_tableWidget")
        self.tab2_targetInventory_tableWidget.setAutoFillBackground(True)

        self.verticalLayout_9.addWidget(self.tab2_targetInventory_tableWidget)

        self.verticalLayout_9.setStretch(2, 1)

        self.gridLayout_4.addWidget(self.frame_3, 0, 1, 1, 1)

        self.frame_4 = QFrame(self.tab_6)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setAutoFillBackground(True)
        self.frame_4.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.frame_4)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.tab2_equipmentInventory_label = QLabel(self.frame_4)
        self.tab2_equipmentInventory_label.setObjectName(u"tab2_equipmentInventory_label")

        self.horizontalLayout_12.addWidget(self.tab2_equipmentInventory_label)

        self.tab2_equipmentRequiredQty_pushButton = QPushButton(self.frame_4)
        self.tab2_equipmentRequiredQty_pushButton.setObjectName(u"tab2_equipmentRequiredQty_pushButton")

        self.horizontalLayout_12.addWidget(self.tab2_equipmentRequiredQty_pushButton)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_12.addItem(self.horizontalSpacer_4)


        self.verticalLayout_10.addLayout(self.horizontalLayout_12)

        self.tab2_equipmentSearch_lineEdit = QLineEdit(self.frame_4)
        self.tab2_equipmentSearch_lineEdit.setObjectName(u"tab2_equipmentSearch_lineEdit")

        self.verticalLayout_10.addWidget(self.tab2_equipmentSearch_lineEdit)

        self.tab2_equipmentInventory_tableWidget = QWidget(self.frame_4)
        self.tab2_equipmentInventory_tableWidget.setObjectName(u"tab2_equipmentInventory_tableWidget")
        self.tab2_equipmentInventory_tableWidget.setAutoFillBackground(True)

        self.verticalLayout_10.addWidget(self.tab2_equipmentInventory_tableWidget)

        self.verticalLayout_10.setStretch(2, 1)

        self.gridLayout_4.addWidget(self.frame_4, 1, 1, 1, 1)


        self.horizontalLayout_13.addLayout(self.gridLayout_4)

        self.tabWidget.addTab(self.tab_6, "")
        self.tab_7 = QWidget()
        self.tab_7.setObjectName(u"tab_7")
        self.verticalLayout_11 = QVBoxLayout(self.tab_7)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.tab3_period_label = QLabel(self.tab_7)
        self.tab3_period_label.setObjectName(u"tab3_period_label")

        self.horizontalLayout_14.addWidget(self.tab3_period_label)

        self.tab3_startDate_lineEdit = QLineEdit(self.tab_7)
        self.tab3_startDate_lineEdit.setObjectName(u"tab3_startDate_lineEdit")

        self.horizontalLayout_14.addWidget(self.tab3_startDate_lineEdit)

        self.label_9 = QLabel(self.tab_7)
        self.label_9.setObjectName(u"label_9")

        self.horizontalLayout_14.addWidget(self.label_9)

        self.tab3_endDate_lineEdit = QLineEdit(self.tab_7)
        self.tab3_endDate_lineEdit.setObjectName(u"tab3_endDate_lineEdit")

        self.horizontalLayout_14.addWidget(self.tab3_endDate_lineEdit)

        self.tab3_itemGroup_label = QLabel(self.tab_7)
        self.tab3_itemGroup_label.setObjectName(u"tab3_itemGroup_label")

        self.horizontalLayout_14.addWidget(self.tab3_itemGroup_label)

        self.tab3_itemGroup_comboBox = QComboBox(self.tab_7)
        self.tab3_itemGroup_comboBox.setObjectName(u"tab3_itemGroup_comboBox")

        self.horizontalLayout_14.addWidget(self.tab3_itemGroup_comboBox)

        self.tab3_division_label = QLabel(self.tab_7)
        self.tab3_division_label.setObjectName(u"tab3_division_label")

        self.horizontalLayout_14.addWidget(self.tab3_division_label)

        self.tab3_division_comboBox = QComboBox(self.tab_7)
        self.tab3_division_comboBox.setObjectName(u"tab3_division_comboBox")

        self.horizontalLayout_14.addWidget(self.tab3_division_comboBox)

        self.tab3_exchangeRate_label = QLabel(self.tab_7)
        self.tab3_exchangeRate_label.setObjectName(u"tab3_exchangeRate_label")

        self.horizontalLayout_14.addWidget(self.tab3_exchangeRate_label)

        self.tab3_exchangeRate_lineEdit = QLineEdit(self.tab_7)
        self.tab3_exchangeRate_lineEdit.setObjectName(u"tab3_exchangeRate_lineEdit")

        self.horizontalLayout_14.addWidget(self.tab3_exchangeRate_lineEdit)

        self.tab3_exportEcvelCsv_pushButton = QPushButton(self.tab_7)
        self.tab3_exportEcvelCsv_pushButton.setObjectName(u"tab3_exportEcvelCsv_pushButton")

        self.horizontalLayout_14.addWidget(self.tab3_exportEcvelCsv_pushButton)


        self.verticalLayout_11.addLayout(self.horizontalLayout_14)

        self.tab3_periodDetail_tableWidget = QWidget(self.tab_7)
        self.tab3_periodDetail_tableWidget.setObjectName(u"tab3_periodDetail_tableWidget")
        self.tab3_periodDetail_tableWidget.setAutoFillBackground(True)

        self.verticalLayout_11.addWidget(self.tab3_periodDetail_tableWidget)

        self.tab3_itemGroupSummary_tableWidget = QWidget(self.tab_7)
        self.tab3_itemGroupSummary_tableWidget.setObjectName(u"tab3_itemGroupSummary_tableWidget")
        self.tab3_itemGroupSummary_tableWidget.setAutoFillBackground(True)

        self.verticalLayout_11.addWidget(self.tab3_itemGroupSummary_tableWidget)

        self.verticalLayout_11.setStretch(1, 10)
        self.verticalLayout_11.setStretch(2, 5)
        self.tabWidget.addTab(self.tab_7, "")
        self.tab_8 = QWidget()
        self.tab_8.setObjectName(u"tab_8")
        self.gridLayoutWidget_3 = QWidget(self.tab_8)
        self.gridLayoutWidget_3.setObjectName(u"gridLayoutWidget_3")
        self.gridLayoutWidget_3.setGeometry(QRect(210, 90, 160, 80))
        self.gridLayout_5 = QGridLayout(self.gridLayoutWidget_3)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.gridLayoutWidget_3)
        self.label.setObjectName(u"label")

        self.gridLayout_5.addWidget(self.label, 0, 0, 1, 1)

        self.comboBox = QComboBox(self.gridLayoutWidget_3)
        self.comboBox.setObjectName(u"comboBox")

        self.gridLayout_5.addWidget(self.comboBox, 0, 1, 1, 1)

        self.tabWidget.addTab(self.tab_8, "")

        self.verticalLayout_4.addWidget(self.tabWidget)


        self.retranslateUi(Form)

        self.tabWidget.setCurrentIndex(2)


        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.tab1_totalPrice_label.setText(QCoreApplication.translate("Form", u"\uae08\uc561", None))
        self.tab1_source_label.setText(QCoreApplication.translate("Form", u"\uac70\ub798/\ubd88\ucd9c\ucc98", None))
        self.tab1_division_label.setText(QCoreApplication.translate("Form", u"\uad6c\ubd84", None))
        self.tab1_unitPrice_label.setText(QCoreApplication.translate("Form", u"\ub2e8\uac00", None))
        self.tab1_date_label.setText(QCoreApplication.translate("Form", u"\ub0a0\uc9dc", None))
        self.tab1_targetID_label.setText(QCoreApplication.translate("Form", u"\ub300\uc0c1 ID", None))
        self.tab1_contact_label.setText(QCoreApplication.translate("Form", u"\uc5f0\ub77d\ucc98", None))
        self.tab1_itemName_label.setText(QCoreApplication.translate("Form", u"\ud488\ubaa9\uba85", None))
        self.tab1_itemCode_label.setText(QCoreApplication.translate("Form", u"\ud488\ubaa9\ucf54\ub4dc", None))
        self.tab1_quantity_label.setText(QCoreApplication.translate("Form", u"\uc218\ub7c9", None))
        self.tab1_note_label.setText(QCoreApplication.translate("Form", u"\ube44\uace0", None))
        self.tab1_manager_label.setText(QCoreApplication.translate("Form", u"\ub2f4\ub2f9\uc790", None))
        self.tab1_itemGroup_label.setText(QCoreApplication.translate("Form", u"\ud488\ubaa9\uad70", None))
        self.tab1_id_label.setText(QCoreApplication.translate("Form", u"ID", None))
        self.tab1_new_pushButton.setText(QCoreApplication.translate("Form", u"\uc2e0\uaddc", None))
        self.tab1_save_pushButton.setText(QCoreApplication.translate("Form", u"\uc800\uc7a5", None))
        self.tab1_barcodeLink_pushButton.setText(QCoreApplication.translate("Form", u"\ubc14\ucf54\ub4dc \uc5f0\ub3d9(\ub3d9\uae30\ud654)", None))
        self.tab1_delete_pushButton.setText(QCoreApplication.translate("Form", u"\uc0ad\uc81c", None))
        self.tab1_exportEcvelCsv_pushButton.setText(QCoreApplication.translate("Form", u"\uc5d1\uc140/CSV \ub0b4\ubcf4\ub0b4\uae30", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), QCoreApplication.translate("Form", u"\uba54\uc778\uc2dc\ud2b8", None))
        self.tab2_waferInventory_label.setText(QCoreApplication.translate("Form", u"\uc6e8\uc774\ud37c \ubcf4\uc720\ud604\ud669", None))
        self.tab2_waferRequiredQty_pushButton.setText(QCoreApplication.translate("Form", u"\ud544\uc694\uc218\ub7c9 \uc785\ub825", None))
        self.tab2_gasInventory_label.setText(QCoreApplication.translate("Form", u"\uac00\uc2a4 \ubcf4\uc720\ud604\ud669", None))
        self.tab2_gasRequiredQty_pushButton.setText(QCoreApplication.translate("Form", u"\ud544\uc694\uc218\ub7c9 \uc785\ub825", None))
        self.tab2_targetInventory_label.setText(QCoreApplication.translate("Form", u"\ud0c0\uac9f \ubcf4\uc720\ud604\ud669", None))
        self.tab2_targetRequiredQty_pushButton.setText(QCoreApplication.translate("Form", u"\ud544\uc694\uc218\ub7c9 \uc785\ub825", None))
        self.tab2_equipmentInventory_label.setText(QCoreApplication.translate("Form", u"\uae30\uc790\uc7ac \ubcf4\uc720\ud604\ud669", None))
        self.tab2_equipmentRequiredQty_pushButton.setText(QCoreApplication.translate("Form", u"\ud544\uc694\uc218\ub7c9 \uc785\ub825", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_6), QCoreApplication.translate("Form", u"\ud488\ubaa9\ubcc4 \uc138\ubb34\ubcf4\uc720\ud604\ud669", None))
        self.tab3_period_label.setText(QCoreApplication.translate("Form", u"\uc870\ud68c\uae30\uac04", None))
        self.label_9.setText(QCoreApplication.translate("Form", u"~", None))
        self.tab3_itemGroup_label.setText(QCoreApplication.translate("Form", u"\ud488\ubaa9\uad70:", None))
        self.tab3_division_label.setText(QCoreApplication.translate("Form", u"\uad6c\ubd84:", None))
        self.tab3_exchangeRate_label.setText(QCoreApplication.translate("Form", u"\ud658\uc728:", None))
        self.tab3_exportEcvelCsv_pushButton.setText(QCoreApplication.translate("Form", u"\uc5d1\uc140/CSV \ub0b4\ubcf4\ub0b4\uae30", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_7), QCoreApplication.translate("Form", u"\uae30\uac04\ubcc4 \uc7ac\uace0 \uc870\ud68c", None))
        self.label.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_8), QCoreApplication.translate("Form", u"\ubc14\ucf54\ub4dc \uc0dd\uc131/\ucd9c\ub825", None))
    # retranslateUi

