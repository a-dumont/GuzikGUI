"""
This is the main application file
"""
import sys
import numpy as np
import matplotlib.pyplot as plt
import threading
from PyQt5.QtWidgets import QApplication, QDialog, QMainWindow, QMessageBox

import Modes
import Plots

try:
    del Plots.BlankPlot
    del Modes.BlankMode
except:
    pass

from GUI import Window

class GuzikOScope(object):

    def __init__(self, guzik=None, fig=None, axes=None):

        if fig == None and axes == None:
            self.fig, ax = plt.subplots()
            self.axes = [ax]
        else:
            self.fig = fig
            self.axes = axes

        if guzik == None:
            self.guzik = Modes.dummy_guzik()
        else:
            self.guzik = guzik

        self._setAvailableModes()
        self._setAvailablePlots()

        self._buffer = None

        self.setCurrentMode('TimeSeries')
        self.setCurrentPlot('OneDimPlot')

        return None

    def __call__(self):
        currentMode = getattr(self,'_currentMode')
        currentPlot = getattr(self,'_currentPlot')
        setattr(self,'_buffer',currentMode())
        currentPlot.updatePlot(getattr(self,'_buffer'))
        return None

    def getNewData(self):
        currentMode = getattr(self,'_currentMode')
        setattr(self,'_buffer',currentMode())
        return getattr(self,'_buffer')

    def getData(self):
        return getattr(self,'_buffer')

    def updatePlot(self, rescale=True):
        currentPlot = getattr(self,'_currentPlot')
        currentPlot.updatePlot(getattr(self,'_buffer'),rescale)
        return None

    def _setAvailableModes(self):
        availableModes = [getattr(Modes,i) for i in dir(Modes)]
        availableModes = [i for i in availableModes if type(i) == type]
        availableModes = [i for i in availableModes if i != Modes.dummy_guzik]
        availableModes = {i.__name__:i for i in availableModes}
        setattr(self,'_availableModes',availableModes)
        return None

    def getAvailableModes(self):
        return getattr(self,'_availableModes')

    def setCurrentMode(self,modeStr):
        availableModes = getattr(self,'_availableModes')
        assert modeStr in availableModes.keys(), "Mode %s not in available modes."%modeStr
        currentMode = availableModes[modeStr](self.guzik)
        setattr(self,'_currentMode',currentMode)
        setattr(self,'_buffer',currentMode.output)
        return

    def getCurrentMode(self):
        mode = getattr(self,'_currentMode')
        return {type(mode).__name__:mode}

    def _setAvailablePlots(self):
        availablePlots = [getattr(Plots,i) for i in dir(Plots)]
        availablePlots = [i for i in availablePlots if type(i) == type]
        availablePlots = {i.__name__:i for i in availablePlots}
        setattr(self,'_availablePlots',availablePlots)
        return None

    def getAvailablePlots(self):
        return getattr(self,'_availablePlots')

    def setCurrentPlot(self,plotStr):
        availablePlots = getattr(self,'_availablePlots')
        assert plotStr in availablePlots.keys(), "Plot %s not in available plots."%plotStr
        currentPlot = availablePlots[plotStr](self.fig,self.axes)
        setattr(self,'_currentPlot',currentPlot)
        currentPlot.initialOutput(getattr(self,'_buffer'))
        return

    def getCurrentPlot(self):
        plot = getattr(self,'_currentPlot')
        return {type(plot).__name__:plot}

class GuzikOScopeWindow(Window):
    def __init__(self):
        super(GuzikOScopeWindow,self).__init__()

        self.scope = GuzikOScope(self.loadGuzik(), self.fig, self.axes)
        self.readConfigGuzik()

        self.setupGuzikTab()
        self.setupAcquisitionTab()
        self.setupModeTab()
        self.setupPlotTab()

        self.continous = False
        self.averaging = False

        return None

    def setupGuzikTab(self):
        self.pushButton_ReadConfigGuzik.clicked.connect(self.readConfigGuzik)
        self.pushButton_UpdateConfigGuzik.clicked.connect(self.updateConfigGuzik)
        return None

    def setupAcquisitionTab(self):
        self.pushButtonSingle.clicked.connect(self.acquisitionSingle)
        self.pushButtonContinous.clicked.connect(self.acquisitionContinuous)
        self.pushButtonStop.clicked.connect(self.acquisitionStop)
        return None

    def setupModeTab(self):
        self.updateModes()
        self.label_CurrentDomainValue.setText(list(self.scope.getCurrentMode().values())[0].modeDomain)
        self.label_CurrentModeValue.setText(list(self.scope.getCurrentMode().values())[0].modeName)
        self.comboBox_CurrentDomain.currentTextChanged.connect(self.updateModes)
        self.pushButton_SetMode.clicked.connect(self.setMode)
        self.getKwargs()
        return None

    def setupPlotTab(self):
        self.pushButton_ClearPlot.clicked.connect(self.clearPlot)
        self.pushButton_UpdatePlotType.clicked.connect(self.setPlotType)
        self.label_CurrentPlotDimensionValue.setText(getattr(self.scope,'_currentMode').modeDimension)
        self.updatePlotTypes()
        self.label_CurrentPlotTypeValue.setText(self.scope._currentPlot.plotName)
        return None

    def loadGuzik(self):
        try:
            from pyHegel.instruments import guzik_adp7104
            guzik = guzik_adp7104()
            self.label_GuzikType.setText("Guzik ADP7104")
        except:
            guzik = Modes.dummy_guzik()
            self.label_GuzikType.setText("Instance of dummy_guzik")
        return guzik

    def updateConfigGuzik(self):
        self.acquisitionStop()
        channels = []
        gain_dB = []
        if self.checkBox_Channel1.isChecked() == True:
            channels.append(1)
            gain_dB.append(self.doubleSpinBox_Gain1.value())
        if self.checkBox_Channel2.isChecked() == True:
            channels.append(2)
            gain_dB.append(self.doubleSpinBox_Gain2.value())
        if self.checkBox_Channel3.isChecked() == True:
            channels.append(3)
            gain_dB.append(self.doubleSpinBox_Gain3.value())
        if self.checkBox_Channel4.isChecked() == True:
            channels.append(4)
            gain_dB.append(self.doubleSpinBox_Gain4.value())

        n_S_ch = self.spinBox_Samples.value()
        bits_16 = bool(self.comboBox_16bits.currentIndex())

        self.scope.guzik.config(channels=channels,gain_dB=gain_dB,n_S_ch=n_S_ch,bits_16=bits_16)
        self.scope.setCurrentMode(list(self.scope.getCurrentMode().keys())[0])
        self.clearPlot()
        return None

    def readConfigGuzik(self):
        config = self.scope.guzik.config()

        channelsUI = [None,None,None,None]
        channelsUI[0] = self.checkBox_Channel1
        channelsUI[1] = self.checkBox_Channel2
        channelsUI[2] = self.checkBox_Channel3
        channelsUI[3] = self.checkBox_Channel4

        gainUI = [None,None,None,None]
        gainUI[0] = self.doubleSpinBox_Gain1
        gainUI[1] = self.doubleSpinBox_Gain2
        gainUI[2] = self.doubleSpinBox_Gain3
        gainUI[3] = self.doubleSpinBox_Gain4

        channels = config['channels'].split(",")
        channels = [int(string[-1])-1 for string in channels]
        gain = config['gain_dB']

        for i in range(len(channels)):
            channelsUI[channels[i]].setChecked(True)
            gainUI[channels[i]].setValue(gain[i])

        self.spinBox_Samples.setValue(config['n_S_ch'])
        self.comboBox_16bits.setCurrentIndex(int(config["bits_16"]))

        return None

    def acquisitionSingle(self):
        self.acquisitionStop()
        self.scope()
        if self.comboBox_Averaging.currentIndex() != 0:
            n = 1.0
            self.averaging = True
            self.scope()
            _buffer = self.scope.getData()
            while n < self.spinBox_Averaging.value() and self.averaging == True:
                _buffer2 = self.scope.getNewData()
                for i in range(len(_buffer)):
                    for key in _buffer[i].keys():
                        if type(_buffer[i][key]) == np.ndarray:
                            _buffer[i][key] = (n*_buffer[i][key]+_buffer2[i][key])/(n+1)
                setattr(self.scope,'_buffer',_buffer)
                self.scope.updatePlot(rescale=False)
                n += 1.0
            self.averaging = False
        return None

    def acquisitionContinuous(self):
        self.acquisitionStop()
        self.continous = True
        if self.comboBox_Averaging.currentIndex() == 0:
            while self.continous == True:
                self.scope()
        else:
            n = 1.0
            self.averaging = True
            self.scope()
            _buffer = getattr(self.scope,'_buffer')
            while self.averaging == True:
                _buffer2 = self.scope.getNewData()
                for i in range(len(_buffer)):
                    for key in _buffer[i].keys():
                        if type(_buffer[i][key]) == np.ndarray:
                            _buffer[i][key] = (n*_buffer[i][key]+_buffer2[i][key])/(n+1)
                setattr(self.scope,'_buffer',_buffer)
                self.scope.updatePlot(rescale=False)
                n += 1.0
            self.averaging = False
        return None

    def acquisitionStop(self):
        self.continous = False
        self.averaging = False
        return None

    def getKwargs(self):
        kwargs = getattr(self.scope,"_currentMode").kwargs
        keys = list(kwargs.keys())

        self.label_ModeParameter1.setText(keys[0])
        self.label_ModeParameter1Value.setText(str(kwargs[keys[0]]))
        self.doubleSpinBox_ModeParameter1.setValue(float(kwargs[keys[0]]))

        self.label_ModeParameter2.setText(keys[1])
        self.label_ModeParameter2Value.setText(str(kwargs[keys[1]]))
        self.doubleSpinBox_ModeParameter2.setValue(float(kwargs[keys[1]]))

        self.label_ModeParameter3.setText(keys[2])
        self.label_ModeParameter3Value.setText(str(kwargs[keys[2]]))
        self.doubleSpinBox_ModeParameter3.setValue(float(kwargs[keys[2]]))
        return None

    def updateKwargs(self):
        kwargs = getattr(self.scope,"_currentMode").kwargs
        keys = list(kwargs.keys())

        kwargs[keys[0]] = self.doubleSpinBox_ModeParameter1.value()
        kwargs[keys[1]] = self.doubleSpinBox_ModeParameter2.value()
        kwargs[keys[2]] = self.doubleSpinBox_ModeParameter3.value()

        setattr(self.scope._currentMode,"kwargs",kwargs)
        setattr(self.scope._currentMode,'output',self.scope._currentMode._initializeOutput())
        return None

    def updateModes(self):
        domain = self.comboBox_CurrentDomain.currentText()
        modes = self.scope.getAvailableModes()

        modes = {i:modes[i] for i in sorted(modes, key=lambda k : modes[k].modeName)}

        for i in range(self.comboBox_CurrentMode.count()):
            self.comboBox_CurrentMode.removeItem(0)

        if domain == "Time":
            for key in modes.keys():
                if modes[key].modeDomain == "Time":
                    self.comboBox_CurrentMode.addItem(modes[key].modeName,key)

        if domain == "Frequency":
            for key in modes.keys():
                if modes[key].modeDomain == "Frequency":
                    self.comboBox_CurrentMode.addItem(modes[key].modeName,key)

        self.getKwargs()
        return None

    def setMode(self):
        self.acquisitionStop()
        curModeStr = list(self.scope.getCurrentMode().keys())[0]
        modeStr = self.comboBox_CurrentMode.currentData()
        self.scope.setCurrentMode(modeStr)
        if curModeStr == modeStr:
            self.updateKwargs()
            setattr(self.scope,'_buffer',self.scope._currentMode.output)
        self.scope.setCurrentPlot(self.scope.getCurrentMode()[modeStr].plotType)
        self.label_CurrentDomainValue.setText(list(self.scope.getCurrentMode().values())[0].modeDomain)
        self.label_CurrentModeValue.setText(list(self.scope.getCurrentMode().values())[0].modeName)
        self.updatePlotTypes()
        self.clearPlot()
        self.getKwargs()
        return None

    def clearPlot(self):
        self.acquisitionStop()
        self.scope.setCurrentPlot(list(self.scope.getCurrentPlot().keys())[0])
        for ax in self.axes:
            for line in ax.lines:
                line.set_ydata(line.get_ydata()*0)
        self.fig.canvas.draw_idle()
        self.fig.canvas.flush_events()
        return None

    def updatePlotTypes(self):
        dimension = self.label_CurrentPlotDimensionValue.text()
        plotTypes = self.scope.getAvailablePlots()

        plotTypes = {i:plotTypes[i] for i in sorted(plotTypes, key=lambda k : plotTypes[k].plotName)}

        for i in range(self.comboBox_PlotType.count()):
            self.comboBox_PlotType.removeItem(0)

        if dimension == "1D":
            for key in plotTypes.keys():
                if plotTypes[key].plotDimension == "1D":
                    self.comboBox_PlotType.addItem(plotTypes[key].plotName,key)

        if dimension == "2D":
            for key in plotTypes.keys():
                if plotTypes[key].plotDimension == "2D":
                    self.comboBox_PlotType.addItem(plotTypes[key].plotName,key)

        return None

    def setPlotType(self):
        self.acquisitionStop()
        plotStr = self.comboBox_PlotType.currentData()
        self.scope.setCurrentPlot(plotStr)
        self.label_CurrentPlotTypeValue.setText(self.scope._currentPlot.plotName)
        return None

def launch():
    app = QApplication(sys.argv)
    win = GuzikOScopeWindow()
    win.show()
    return app, win
#if __name__ == "__main__":
#    app = QApplication(sys.argv)
#    win = GuzikOScopeWindow()
#    win.show()
#    sys.exit(app.exec())
