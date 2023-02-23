# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GuzikLayout.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1063, 781)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.mpl_widget = QtWidgets.QWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mpl_widget.sizePolicy().hasHeightForWidth())
        self.mpl_widget.setSizePolicy(sizePolicy)
        self.mpl_widget.setMinimumSize(QtCore.QSize(0, 600))
        self.mpl_widget.setObjectName("mpl_widget")
        self.mpl_layout = QtWidgets.QVBoxLayout(self.mpl_widget)
        self.mpl_layout.setObjectName("mpl_layout")
        self.verticalLayout.addWidget(self.mpl_widget)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)
        self.tabWidget.setMinimumSize(QtCore.QSize(0, 150))
        self.tabWidget.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.tabWidget.setTabBarAutoHide(False)
        self.tabWidget.setObjectName("tabWidget")
        self.tabGuzik = QtWidgets.QWidget()
        self.tabGuzik.setObjectName("tabGuzik")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.tabGuzik)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_GuzikConfig = QtWidgets.QLabel(self.tabGuzik)
        self.label_GuzikConfig.setObjectName("label_GuzikConfig")
        self.verticalLayout_5.addWidget(self.label_GuzikConfig)
        self.label_GuzikType = QtWidgets.QLabel(self.tabGuzik)
        self.label_GuzikType.setObjectName("label_GuzikType")
        self.verticalLayout_5.addWidget(self.label_GuzikType)
        self.pushButton_ReadConfigGuzik = QtWidgets.QPushButton(self.tabGuzik)
        self.pushButton_ReadConfigGuzik.setObjectName("pushButton_ReadConfigGuzik")
        self.verticalLayout_5.addWidget(self.pushButton_ReadConfigGuzik)
        self.pushButton_UpdateConfigGuzik = QtWidgets.QPushButton(self.tabGuzik)
        self.pushButton_UpdateConfigGuzik.setObjectName("pushButton_UpdateConfigGuzik")
        self.verticalLayout_5.addWidget(self.pushButton_UpdateConfigGuzik)
        self.horizontalLayout_3.addLayout(self.verticalLayout_5)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.labelChannels = QtWidgets.QLabel(self.tabGuzik)
        self.labelChannels.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.labelChannels.setObjectName("labelChannels")
        self.verticalLayout_4.addWidget(self.labelChannels)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.checkBox_Channel1 = QtWidgets.QCheckBox(self.tabGuzik)
        self.checkBox_Channel1.setObjectName("checkBox_Channel1")
        self.horizontalLayout_6.addWidget(self.checkBox_Channel1)
        self.checkBox_Channel2 = QtWidgets.QCheckBox(self.tabGuzik)
        self.checkBox_Channel2.setObjectName("checkBox_Channel2")
        self.horizontalLayout_6.addWidget(self.checkBox_Channel2)
        self.verticalLayout_4.addLayout(self.horizontalLayout_6)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.checkBox_Channel3 = QtWidgets.QCheckBox(self.tabGuzik)
        self.checkBox_Channel3.setObjectName("checkBox_Channel3")
        self.horizontalLayout.addWidget(self.checkBox_Channel3)
        self.checkBox_Channel4 = QtWidgets.QCheckBox(self.tabGuzik)
        self.checkBox_Channel4.setObjectName("checkBox_Channel4")
        self.horizontalLayout.addWidget(self.checkBox_Channel4)
        self.verticalLayout_4.addLayout(self.horizontalLayout)
        self.horizontalLayout_3.addLayout(self.verticalLayout_4)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.label_Gain = QtWidgets.QLabel(self.tabGuzik)
        self.label_Gain.setObjectName("label_Gain")
        self.verticalLayout_7.addWidget(self.label_Gain)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.doubleSpinBox_Gain1 = QtWidgets.QDoubleSpinBox(self.tabGuzik)
        self.doubleSpinBox_Gain1.setMinimum(-25.0)
        self.doubleSpinBox_Gain1.setMaximum(32.0)
        self.doubleSpinBox_Gain1.setObjectName("doubleSpinBox_Gain1")
        self.horizontalLayout_8.addWidget(self.doubleSpinBox_Gain1)
        self.doubleSpinBox_Gain2 = QtWidgets.QDoubleSpinBox(self.tabGuzik)
        self.doubleSpinBox_Gain2.setMinimum(-25.0)
        self.doubleSpinBox_Gain2.setMaximum(32.0)
        self.doubleSpinBox_Gain2.setObjectName("doubleSpinBox_Gain2")
        self.horizontalLayout_8.addWidget(self.doubleSpinBox_Gain2)
        self.verticalLayout_7.addLayout(self.horizontalLayout_8)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.doubleSpinBox_Gain3 = QtWidgets.QDoubleSpinBox(self.tabGuzik)
        self.doubleSpinBox_Gain3.setMinimum(-25.0)
        self.doubleSpinBox_Gain3.setMaximum(32.0)
        self.doubleSpinBox_Gain3.setObjectName("doubleSpinBox_Gain3")
        self.horizontalLayout_7.addWidget(self.doubleSpinBox_Gain3)
        self.doubleSpinBox_Gain4 = QtWidgets.QDoubleSpinBox(self.tabGuzik)
        self.doubleSpinBox_Gain4.setMinimum(-25.0)
        self.doubleSpinBox_Gain4.setMaximum(32.0)
        self.doubleSpinBox_Gain4.setObjectName("doubleSpinBox_Gain4")
        self.horizontalLayout_7.addWidget(self.doubleSpinBox_Gain4)
        self.verticalLayout_7.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_4.addLayout(self.verticalLayout_7)
        self.verticalLayout_3.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_3.addLayout(self.verticalLayout_3)
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout()
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.label_n_S_ch = QtWidgets.QLabel(self.tabGuzik)
        self.label_n_S_ch.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_n_S_ch.setObjectName("label_n_S_ch")
        self.verticalLayout_10.addWidget(self.label_n_S_ch)
        self.spinBox_Samples = QtWidgets.QSpinBox(self.tabGuzik)
        self.spinBox_Samples.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.spinBox_Samples.setButtonSymbols(QtWidgets.QAbstractSpinBox.UpDownArrows)
        self.spinBox_Samples.setMaximum(429496729)
        self.spinBox_Samples.setObjectName("spinBox_Samples")
        self.verticalLayout_10.addWidget(self.spinBox_Samples)
        self.horizontalLayout_5.addLayout(self.verticalLayout_10)
        self.verticalLayout_13 = QtWidgets.QVBoxLayout()
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.label_16bits = QtWidgets.QLabel(self.tabGuzik)
        self.label_16bits.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_16bits.setObjectName("label_16bits")
        self.verticalLayout_13.addWidget(self.label_16bits)
        self.comboBox_16bits = QtWidgets.QComboBox(self.tabGuzik)
        self.comboBox_16bits.setObjectName("comboBox_16bits")
        self.comboBox_16bits.addItem("")
        self.comboBox_16bits.addItem("")
        self.verticalLayout_13.addWidget(self.comboBox_16bits)
        self.horizontalLayout_5.addLayout(self.verticalLayout_13)
        self.verticalLayout_6.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_3.addLayout(self.verticalLayout_6)
        self.tabWidget.addTab(self.tabGuzik, "")
        self.tabAcquisition = QtWidgets.QWidget()
        self.tabAcquisition.setObjectName("tabAcquisition")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.tabAcquisition)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout()
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.label_Averaging = QtWidgets.QLabel(self.tabAcquisition)
        self.label_Averaging.setObjectName("label_Averaging")
        self.verticalLayout_11.addWidget(self.label_Averaging)
        self.comboBox_Averaging = QtWidgets.QComboBox(self.tabAcquisition)
        self.comboBox_Averaging.setObjectName("comboBox_Averaging")
        self.comboBox_Averaging.addItem("")
        self.comboBox_Averaging.addItem("")
        self.verticalLayout_11.addWidget(self.comboBox_Averaging)
        self.spinBox_Averaging = QtWidgets.QSpinBox(self.tabAcquisition)
        self.spinBox_Averaging.setMinimum(1)
        self.spinBox_Averaging.setMaximum(1000)
        self.spinBox_Averaging.setObjectName("spinBox_Averaging")
        self.verticalLayout_11.addWidget(self.spinBox_Averaging)
        self.horizontalLayout_2.addLayout(self.verticalLayout_11)
        self.verticalLayout_16 = QtWidgets.QVBoxLayout()
        self.verticalLayout_16.setObjectName("verticalLayout_16")
        self.pushButtonSingle = QtWidgets.QPushButton(self.tabAcquisition)
        self.pushButtonSingle.setAutoDefault(False)
        self.pushButtonSingle.setDefault(False)
        self.pushButtonSingle.setFlat(False)
        self.pushButtonSingle.setObjectName("pushButtonSingle")
        self.verticalLayout_16.addWidget(self.pushButtonSingle)
        self.pushButtonContinous = QtWidgets.QPushButton(self.tabAcquisition)
        self.pushButtonContinous.setObjectName("pushButtonContinous")
        self.verticalLayout_16.addWidget(self.pushButtonContinous)
        self.pushButtonStop = QtWidgets.QPushButton(self.tabAcquisition)
        self.pushButtonStop.setObjectName("pushButtonStop")
        self.verticalLayout_16.addWidget(self.pushButtonStop)
        self.horizontalLayout_2.addLayout(self.verticalLayout_16)
        self.tabWidget.addTab(self.tabAcquisition, "")
        self.tabMode = QtWidgets.QWidget()
        self.tabMode.setObjectName("tabMode")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.tabMode)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.verticalLayout_15 = QtWidgets.QVBoxLayout()
        self.verticalLayout_15.setObjectName("verticalLayout_15")
        self.horizontalLayout_17 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_17.setObjectName("horizontalLayout_17")
        self.label_DomainSelect = QtWidgets.QLabel(self.tabMode)
        self.label_DomainSelect.setObjectName("label_DomainSelect")
        self.horizontalLayout_17.addWidget(self.label_DomainSelect)
        self.comboBox_CurrentDomain = QtWidgets.QComboBox(self.tabMode)
        self.comboBox_CurrentDomain.setObjectName("comboBox_CurrentDomain")
        self.comboBox_CurrentDomain.addItem("")
        self.comboBox_CurrentDomain.addItem("")
        self.horizontalLayout_17.addWidget(self.comboBox_CurrentDomain)
        self.verticalLayout_15.addLayout(self.horizontalLayout_17)
        self.horizontalLayout_18 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_18.setObjectName("horizontalLayout_18")
        self.label_ModeSelect = QtWidgets.QLabel(self.tabMode)
        self.label_ModeSelect.setObjectName("label_ModeSelect")
        self.horizontalLayout_18.addWidget(self.label_ModeSelect)
        self.comboBox_CurrentMode = QtWidgets.QComboBox(self.tabMode)
        self.comboBox_CurrentMode.setObjectName("comboBox_CurrentMode")
        self.horizontalLayout_18.addWidget(self.comboBox_CurrentMode)
        self.verticalLayout_15.addLayout(self.horizontalLayout_18)
        self.horizontalLayout_9.addLayout(self.verticalLayout_15)
        self.verticalLayout_14 = QtWidgets.QVBoxLayout()
        self.verticalLayout_14.setObjectName("verticalLayout_14")
        self.horizontalLayout_15 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")
        self.label_ModeParameters = QtWidgets.QLabel(self.tabMode)
        self.label_ModeParameters.setObjectName("label_ModeParameters")
        self.horizontalLayout_15.addWidget(self.label_ModeParameters)
        self.label_ModeParameterSelect = QtWidgets.QLabel(self.tabMode)
        self.label_ModeParameterSelect.setObjectName("label_ModeParameterSelect")
        self.horizontalLayout_15.addWidget(self.label_ModeParameterSelect)
        self.label_ModeParameterCurrent = QtWidgets.QLabel(self.tabMode)
        self.label_ModeParameterCurrent.setObjectName("label_ModeParameterCurrent")
        self.horizontalLayout_15.addWidget(self.label_ModeParameterCurrent)
        self.verticalLayout_14.addLayout(self.horizontalLayout_15)
        self.horizontalLayout_20 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_20.setObjectName("horizontalLayout_20")
        self.label_ModeParameter1 = QtWidgets.QLabel(self.tabMode)
        self.label_ModeParameter1.setObjectName("label_ModeParameter1")
        self.horizontalLayout_20.addWidget(self.label_ModeParameter1)
        self.doubleSpinBox = QtWidgets.QDoubleSpinBox(self.tabMode)
        self.doubleSpinBox.setMinimum(-100000000000.0)
        self.doubleSpinBox.setMaximum(1000000000000.0)
        self.doubleSpinBox.setObjectName("doubleSpinBox")
        self.horizontalLayout_20.addWidget(self.doubleSpinBox)
        self.label_ModeParameter1Value = QtWidgets.QLabel(self.tabMode)
        self.label_ModeParameter1Value.setObjectName("label_ModeParameter1Value")
        self.horizontalLayout_20.addWidget(self.label_ModeParameter1Value)
        self.verticalLayout_14.addLayout(self.horizontalLayout_20)
        self.horizontalLayout_21 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_21.setObjectName("horizontalLayout_21")
        self.label_ModeParameter2 = QtWidgets.QLabel(self.tabMode)
        self.label_ModeParameter2.setObjectName("label_ModeParameter2")
        self.horizontalLayout_21.addWidget(self.label_ModeParameter2)
        self.doubleSpinBox_2 = QtWidgets.QDoubleSpinBox(self.tabMode)
        self.doubleSpinBox_2.setMinimum(-100000000000.0)
        self.doubleSpinBox_2.setMaximum(100000000000.0)
        self.doubleSpinBox_2.setObjectName("doubleSpinBox_2")
        self.horizontalLayout_21.addWidget(self.doubleSpinBox_2)
        self.label_ModeParameter2Value = QtWidgets.QLabel(self.tabMode)
        self.label_ModeParameter2Value.setObjectName("label_ModeParameter2Value")
        self.horizontalLayout_21.addWidget(self.label_ModeParameter2Value)
        self.verticalLayout_14.addLayout(self.horizontalLayout_21)
        self.horizontalLayout_19 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_19.setObjectName("horizontalLayout_19")
        self.label_ModeParameter3 = QtWidgets.QLabel(self.tabMode)
        self.label_ModeParameter3.setObjectName("label_ModeParameter3")
        self.horizontalLayout_19.addWidget(self.label_ModeParameter3)
        self.doubleSpinBox_3 = QtWidgets.QDoubleSpinBox(self.tabMode)
        self.doubleSpinBox_3.setMinimum(-100000000000.0)
        self.doubleSpinBox_3.setMaximum(100000000000.0)
        self.doubleSpinBox_3.setObjectName("doubleSpinBox_3")
        self.horizontalLayout_19.addWidget(self.doubleSpinBox_3)
        self.label_ModeParameter3Value = QtWidgets.QLabel(self.tabMode)
        self.label_ModeParameter3Value.setObjectName("label_ModeParameter3Value")
        self.horizontalLayout_19.addWidget(self.label_ModeParameter3Value)
        self.verticalLayout_14.addLayout(self.horizontalLayout_19)
        self.horizontalLayout_9.addLayout(self.verticalLayout_14)
        self.verticalLayout_17 = QtWidgets.QVBoxLayout()
        self.verticalLayout_17.setObjectName("verticalLayout_17")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.label_CurrentDomain = QtWidgets.QLabel(self.tabMode)
        self.label_CurrentDomain.setObjectName("label_CurrentDomain")
        self.horizontalLayout_10.addWidget(self.label_CurrentDomain)
        self.label_CurrentDomainValue = QtWidgets.QLabel(self.tabMode)
        self.label_CurrentDomainValue.setObjectName("label_CurrentDomainValue")
        self.horizontalLayout_10.addWidget(self.label_CurrentDomainValue)
        self.verticalLayout_17.addLayout(self.horizontalLayout_10)
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.label_CurrentMode = QtWidgets.QLabel(self.tabMode)
        self.label_CurrentMode.setObjectName("label_CurrentMode")
        self.horizontalLayout_11.addWidget(self.label_CurrentMode)
        self.label_CurrentModeValue = QtWidgets.QLabel(self.tabMode)
        self.label_CurrentModeValue.setObjectName("label_CurrentModeValue")
        self.horizontalLayout_11.addWidget(self.label_CurrentModeValue)
        self.verticalLayout_17.addLayout(self.horizontalLayout_11)
        self.pushButton_SetMode = QtWidgets.QPushButton(self.tabMode)
        self.pushButton_SetMode.setObjectName("pushButton_SetMode")
        self.verticalLayout_17.addWidget(self.pushButton_SetMode)
        self.horizontalLayout_9.addLayout(self.verticalLayout_17)
        self.tabWidget.addTab(self.tabMode, "")
        self.tabPlot = QtWidgets.QWidget()
        self.tabPlot.setObjectName("tabPlot")
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout(self.tabPlot)
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.verticalLayout_18 = QtWidgets.QVBoxLayout()
        self.verticalLayout_18.setObjectName("verticalLayout_18")
        self.label_CurrentPlotDimension = QtWidgets.QLabel(self.tabPlot)
        self.label_CurrentPlotDimension.setObjectName("label_CurrentPlotDimension")
        self.verticalLayout_18.addWidget(self.label_CurrentPlotDimension)
        self.label_CurrentPlotDimensionValue = QtWidgets.QLabel(self.tabPlot)
        self.label_CurrentPlotDimensionValue.setTextFormat(QtCore.Qt.AutoText)
        self.label_CurrentPlotDimensionValue.setObjectName("label_CurrentPlotDimensionValue")
        self.verticalLayout_18.addWidget(self.label_CurrentPlotDimensionValue)
        self.horizontalLayout_13.addLayout(self.verticalLayout_18)
        self.verticalLayout_20 = QtWidgets.QVBoxLayout()
        self.verticalLayout_20.setObjectName("verticalLayout_20")
        self.label_PlotType = QtWidgets.QLabel(self.tabPlot)
        self.label_PlotType.setObjectName("label_PlotType")
        self.verticalLayout_20.addWidget(self.label_PlotType)
        self.comboBox_PlotType = QtWidgets.QComboBox(self.tabPlot)
        self.comboBox_PlotType.setObjectName("comboBox_PlotType")
        self.verticalLayout_20.addWidget(self.comboBox_PlotType)
        self.horizontalLayout_13.addLayout(self.verticalLayout_20)
        self.verticalLayout_19 = QtWidgets.QVBoxLayout()
        self.verticalLayout_19.setObjectName("verticalLayout_19")
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.label_CurrentPlotType = QtWidgets.QLabel(self.tabPlot)
        self.label_CurrentPlotType.setObjectName("label_CurrentPlotType")
        self.horizontalLayout_12.addWidget(self.label_CurrentPlotType)
        self.label_CurrentPlotTypeValue = QtWidgets.QLabel(self.tabPlot)
        self.label_CurrentPlotTypeValue.setObjectName("label_CurrentPlotTypeValue")
        self.horizontalLayout_12.addWidget(self.label_CurrentPlotTypeValue)
        self.verticalLayout_19.addLayout(self.horizontalLayout_12)
        self.pushButton_UpdatePlotType = QtWidgets.QPushButton(self.tabPlot)
        self.pushButton_UpdatePlotType.setObjectName("pushButton_UpdatePlotType")
        self.verticalLayout_19.addWidget(self.pushButton_UpdatePlotType)
        self.pushButton_ClearPlot = QtWidgets.QPushButton(self.tabPlot)
        self.pushButton_ClearPlot.setObjectName("pushButton_ClearPlot")
        self.verticalLayout_19.addWidget(self.pushButton_ClearPlot)
        self.horizontalLayout_13.addLayout(self.verticalLayout_19)
        self.tabWidget.addTab(self.tabPlot, "")
        self.verticalLayout_2.addWidget(self.tabWidget)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1063, 25))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.menuFile.sizePolicy().hasHeightForWidth())
        self.menuFile.setSizePolicy(sizePolicy)
        self.menuFile.setObjectName("menuFile")
        self.menuEdit = QtWidgets.QMenu(self.menubar)
        self.menuEdit.setObjectName("menuEdit")
        MainWindow.setMenuBar(self.menubar)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Guzik-O-Scope"))
        self.label_GuzikConfig.setText(_translate("MainWindow", "Config"))
        self.label_GuzikType.setText(_translate("MainWindow", "Dummy Guzik"))
        self.pushButton_ReadConfigGuzik.setText(_translate("MainWindow", "Read config"))
        self.pushButton_UpdateConfigGuzik.setText(_translate("MainWindow", "Update config"))
        self.labelChannels.setText(_translate("MainWindow", "Channels"))
        self.checkBox_Channel1.setText(_translate("MainWindow", "Channel 1"))
        self.checkBox_Channel2.setText(_translate("MainWindow", "Channel 2"))
        self.checkBox_Channel3.setText(_translate("MainWindow", "Channel 3"))
        self.checkBox_Channel4.setText(_translate("MainWindow", "Channel 4"))
        self.label_Gain.setText(_translate("MainWindow", "Gain (dB)"))
        self.label_n_S_ch.setText(_translate("MainWindow", "Samples"))
        self.label_16bits.setText(_translate("MainWindow", "16 Bits"))
        self.comboBox_16bits.setItemText(0, _translate("MainWindow", "False"))
        self.comboBox_16bits.setItemText(1, _translate("MainWindow", "True"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabGuzik), _translate("MainWindow", "Guzik"))
        self.label_Averaging.setText(_translate("MainWindow", "Averaging"))
        self.comboBox_Averaging.setItemText(0, _translate("MainWindow", "False"))
        self.comboBox_Averaging.setItemText(1, _translate("MainWindow", "True"))
        self.pushButtonSingle.setText(_translate("MainWindow", "Single"))
        self.pushButtonContinous.setText(_translate("MainWindow", "Continuous"))
        self.pushButtonStop.setText(_translate("MainWindow", "Stop"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabAcquisition), _translate("MainWindow", "Acquisition"))
        self.label_DomainSelect.setText(_translate("MainWindow", "Domain"))
        self.comboBox_CurrentDomain.setItemText(0, _translate("MainWindow", "Time"))
        self.comboBox_CurrentDomain.setItemText(1, _translate("MainWindow", "Frequency"))
        self.label_ModeSelect.setText(_translate("MainWindow", "Mode"))
        self.label_ModeParameters.setText(_translate("MainWindow", "Parameters"))
        self.label_ModeParameterSelect.setText(_translate("MainWindow", "New value"))
        self.label_ModeParameterCurrent.setText(_translate("MainWindow", "Current value"))
        self.label_ModeParameter1.setText(_translate("MainWindow", "Parameter 1"))
        self.label_ModeParameter1Value.setText(_translate("MainWindow", "Value 1"))
        self.label_ModeParameter2.setText(_translate("MainWindow", "Parameter 2"))
        self.label_ModeParameter2Value.setText(_translate("MainWindow", "Value 2"))
        self.label_ModeParameter3.setText(_translate("MainWindow", "Parameter 3"))
        self.label_ModeParameter3Value.setText(_translate("MainWindow", "Value 3"))
        self.label_CurrentDomain.setText(_translate("MainWindow", "Current domain:"))
        self.label_CurrentDomainValue.setText(_translate("MainWindow", "Domain"))
        self.label_CurrentMode.setText(_translate("MainWindow", "Current Mode:"))
        self.label_CurrentModeValue.setText(_translate("MainWindow", "Mode"))
        self.pushButton_SetMode.setText(_translate("MainWindow", "Set Mode"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabMode), _translate("MainWindow", "Mode"))
        self.label_CurrentPlotDimension.setText(_translate("MainWindow", "Dimension"))
        self.label_CurrentPlotDimensionValue.setText(_translate("MainWindow", "Dimension value"))
        self.label_PlotType.setText(_translate("MainWindow", "Plot type"))
        self.label_CurrentPlotType.setText(_translate("MainWindow", "Current plot type:"))
        self.label_CurrentPlotTypeValue.setText(_translate("MainWindow", "type"))
        self.pushButton_UpdatePlotType.setText(_translate("MainWindow", "Update plot type"))
        self.pushButton_ClearPlot.setText(_translate("MainWindow", "Clear plot"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabPlot), _translate("MainWindow", "Plot"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuEdit.setTitle(_translate("MainWindow", "Edit"))
