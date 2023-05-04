"""
Time Series measurement.
"""
import numpy as np
from .Mode import BlankMode
from SignalProcessing.histograms import digitizer_histogram
from SignalProcessing.histograms import digitizer_histogram2D
try:
    from pyHegel.commands import get
except:
    def get(guzik):
        return guzik()

class TimeSeries(BlankMode):

    modeDomain = "Time"
    modeName = "Time series"
    plotType = "OneDimPlot"
    modeDimension = "1D"

    outFmt = {}
    outFmt['xData'] = None
    outFmt["yData"] = None
    outFmt["xLabel"] = "Time"
    outFmt["xUnit"] = "[s]"
    outFmt["yLabel"] = "Voltage"
    outFmt["yUnit"] = "[V]"
    outFmt["label"] = None

    kwargs = {}
    kwargs["Not Used 1"] = 0
    kwargs["Not Used 2"] = 0
    kwargs["Not Used 3"] = 0

    def __init__(self,guzik):

        self.guzik = guzik
        self.output = self._initializeOutput()
        return None

    def __repr__(self):
        return "<TimeSeries object at %s>"%str(hex(id(self)))

    def __str__(self):
        return "Time series mode"

    def __call__(self):

        data = get(self.guzik)

        if self.guzik.config()["Nch"] == 1:
            data = np.array([data])

        ch = self.guzik.config()["channels"]
        ch = ch.split(",")

        assert len(ch) == len(self.output), "Number of channels and outputs do not match."

        for i in range(len(self.output)):
            self.output[i]['yData'] = data[i]

        return [out.copy() for out in self.output]

    def _initializeOutput(self):
        Nch = self.guzik.config()['Nch']
        n_S_ch = self.guzik.config()['n_S_ch']
        ch = self.guzik.config()["channels"]
        ch = ch.split(",")
        dt = self.guzik.config()['sampling_period_ns']*1e-9

        if self.guzik.config()['bits_16'] == True:
            data = np.zeros((Nch,n_S_ch),dtype=np.int16)
        else:
            data = np.zeros((Nch,n_S_ch),dtype=np.uint8)

        output = [self.outFmt.copy() for i in range(data.shape[0])]

        xData = np.linspace(0,n_S_ch*dt,n_S_ch)

        for i in range(len(output)):
            output[i]['xData'] = xData
            output[i]["yData"] = data[i]
            output[i]["label"] = "Channel %s"%ch[i][-1]

        return output

class OneDimHistogram(BlankMode):

    modeDomain = "Time"
    modeName = "1D Histogram"
    plotType = "OneDimPlot"
    modeDimension = "1D"

    outFmt = {}
    outFmt['xData'] = None
    outFmt["yData"] = None
    outFmt["xLabel"] = "Bin"
    outFmt["xUnit"] = ""
    outFmt["yLabel"] = "Count"
    outFmt["yUnit"] = ""
    outFmt["label"] = None

    kwargs = {}
    kwargs["Not Used 1"] = 0
    kwargs["Not Used 2"] = 0
    kwargs["Not Used 3"] = 0

    def __init__(self,guzik):

        self.guzik = guzik
        self.output = self._initializeOutput()
        return None

    def __repr__(self):
        return "<1DHistogram object at %s>"%str(hex(id(self)))

    def __str__(self):
        return "1D Histogram mode"

    def __call__(self):

        data = get(self.guzik)

        if self.guzik.config()["Nch"] == 1:
            data = np.array([data])

        ch = self.guzik.config()["channels"]
        ch = ch.split(",")

        assert len(ch) == len(self.output), "Number of channels and outputs do not match."

        for i in range(len(self.output)):
            self.output[i]["yData"] = digitizer_histogram(data[i],self.nbits)[0:1<<self.nbits_out]

        return [out.copy() for out in self.output]

    def _initializeOutput(self):
        Nch = self.guzik.config()['Nch']
        n_S_ch = self.guzik.config()['n_S_ch']
        ch = self.guzik.config()["channels"]
        ch = ch.split(",")

        if self.guzik.config()["bits_16"] == True:
            self.nbits = 16
            self.nbits_out = 10
        else:
            self.nbits = 8
            self.nbits_out = 8

        if self.guzik.config()['bits_16'] == True:
            data = np.zeros((Nch,n_S_ch),dtype=np.int16)
        else:
            data = np.zeros((Nch,n_S_ch),dtype=np.uint8)

        output = [self.outFmt.copy() for i in range(data.shape[0])]

        xData = np.linspace(0,(1<<self.nbits_out)-1,1<<self.nbits_out)

        for i in range(len(output)):
            output[i]['xData'] = xData
            output[i]["yData"] = digitizer_histogram(data[i],self.nbits)[0:1<<self.nbits_out]
            output[i]["label"] = "Channel %s"%ch[i][-1]

        return output

class TwoDimHistogram(BlankMode):

    modeDomain = "Time"
    modeName = "2D Histogram"
    plotType = "TwoDimPlotCMap"
    modeDimension = "2D"

    outFmt = {}
    outFmt['xData'] = None
    outFmt["yData"] = None
    outFmt["zData"] = None
    outFmt["xLabel"] = "Bin"
    outFmt["xUnit"] = ""
    outFmt["yLabel"] = "Bin"
    outFmt["yUnit"] = ""
    outFmt["zLabel"] = "Count"
    outFmt["zUnit"] = ""
    outFmt["label"] = None

    kwargs = {}
    kwargs["Not Used 1"] = 0
    kwargs["Not Used 2"] = 0
    kwargs["Not Used 3"] = 0

    def __init__(self,guzik):

        super(TwoDimHistogram,self).__init__(guzik)

        if self.guzik.config()["bits_16"] is True:
            self.nbits = 16
            self.nbits_out = 10
        else:
            self.nbits = 8
            self.nbits_out = 8

    def __repr__(self):
        return "<2DHistogram object at %s>"%str(hex(id(self)))

    def __str__(self):
        return "2D Histogram mode"

    def __call__(self):

        Nch = self.guzik.config()['Nch']
        assert Nch == 2, 'Must have two channels'

        data = get(self.guzik)

        res = digitizer_histogram2D(data[0],data[1],self.nbits)[0:1<<self.nbits_out,0:1<<self.nbits_out]
        self.output[0]["zData"] = res

        return [out.copy() for out in self.output]

    def _initializeOutput(self):
        Nch = self.guzik.config()['Nch']
        assert Nch == 2, 'Must have two channels'
        n_S_ch = self.guzik.config()['n_S_ch']
        ch = self.guzik.config()["channels"]
        ch = ch.split(",")

        if self.guzik.config()["bits_16"] == True:
            self.nbits = 16
            self.nbits_out = 10
        else:
            self.nbits = 8
            self.nbits_out = 8

        if self.guzik.config()['bits_16'] == True:
            data = np.zeros((Nch,n_S_ch),dtype=np.int16)
        else:
            data = np.zeros((Nch,n_S_ch),dtype=np.uint8)

        output = [self.outFmt.copy()]

        xData = np.linspace(0,(1<<self.nbits_out)-1,1<<self.nbits_out)
        yData = np.linspace(0,(1<<self.nbits_out)-1,1<<self.nbits_out)

        output[0]['xData'] = xData
        output[0]['yData'] = yData
        output[0]["zData"] = digitizer_histogram2D(data[0],data[1],self.nbits)[0:1<<self.nbits_out,0:1<<self.nbits_out]
        output[0]["label"] = "Channels %s-%s"%(ch[0][-1],ch[1][-1])

        return output

