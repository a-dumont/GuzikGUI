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
        self.setCurrentPlot('BlankPlot')

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
        setattr(self,'_buffer',currentMode.getDummyOutput())
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

        self.scope = GuzikOScope(None, self.fig, self.axes)
        self.readConfigGuzik()

        self.setupGuzikTab()
        self.setupAcquisitionTab()

        self.continous = False

        return None

    def setupGuzikTab(self):
        self.pushButton_LoadGuzik.clicked.connect(self.loadGuzik)
        self.pushButton_ReadConfigGuzik.clicked.connect(self.readConfigGuzik)
        self.pushButton_UpdateConfigGuzik.clicked.connect(self.updateConfigGuzik)
        return None

    def setupAcquisitionTab(self):
        self.pushButtonSingle.clicked.connect(self.acquisitionSingle)
        self.pushButtonContinous.clicked.connect(self.acquisitionContinuous)
        self.pushButtonStop.clicked.connect(self.acquisitionStop)
        return None

    def setupModeTab(self):
        return None

    def setupPlotTab(self):
        return None

    def loadGuzik(self):
        return None

    def updateConfigGuzik(self):
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
        self.scope.setCurrentPlot(list(self.scope.getCurrentPlot().keys())[0])
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
        self.continous = False
        self.averaging = False
        if self.comboBox_Averaging.currentIndex() == 0:
            self.scope()
        else:
            n = 1
            self.averaging = True
            self.scope()
            _buffer = getattr(self.scope,'_buffer')
            while n < self.spinBox_Averaging.value() and self.averaging == True:
                _buffer2 = self.scope.getNewData()
                for i in range(len(_buffer)):
                    for key in _buffer[i].keys():
                        if type(_buffer[i][key]) == np.ndarray:
                            _buffer[i][key] = (n*_buffer[i][key]+_buffer2[i][key])/(n+1)
                setattr(self.scope,'_buffer',_buffer)
                self.scope.updatePlot(rescale=False)
                n += 1
            self.averaging = False
        return None

    def acquisitionContinuous(self):
        self.continous = True
        if self.comboBox_Averaging.currentIndex() == 0:
            while self.continous == True:
                self.scope()
        else:
            n = 1
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
                n += 1
            self.averaging = False
        return None

    def acquisitionStop(self):
        self.continous = False
        self.averaging = False
        return None



if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = GuzikOScopeWindow()
    #win.scope.setCurrentMode('OneDimHistogram')
    #win.scope.setCurrentPlot('BlankPlot')
    win.show()
    for i in range(100):
        win.scope()
    sys.exit(app.exec())
