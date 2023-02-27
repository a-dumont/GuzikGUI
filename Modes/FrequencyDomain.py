"""
Time Series measurement.
"""
import numpy as np
from .Mode import BlankMode
from SignalProcessing.fft import digitizer_rFFT
from SignalProcessing.fft import digitizer_rFFT_cuda

try:
    from pyHegel.commands import get
except:
    def get(guzik):
        return guzik()

class VoltageSpectrum(BlankMode):

    modeDomain = "Frequency"
    modeName = "Voltage Spectrum"
    plotType = "OneDimPlot"
    modeDimension = "1D"

    outFmt = {}
    outFmt['xData'] = None
    outFmt["yData"] = None
    outFmt["xLabel"] = "Frequency"
    outFmt["xUnit"] = "[Hz]"
    outFmt["yLabel"] = "Voltage spectrum"
    outFmt["yUnit"] = r"[V/$\sqrt{\rm Hz}$]"
    outFmt["label"] = None

    kwargs = {}
    kwargs["Block Size"] = 2048
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

        conv = self.guzik.config()['conv_resolution']
        offset = self.guzik.config()['conv_offset']
        size = int(self.kwargs['Block Size']/2+1)

        assert len(ch) == len(self.output), "Number of channels and outputs do not match."

        for i in range(len(self.output)):
            result = np.abs(digitizer_rFFT(data[i],int(self.kwargs['Block Size']),conv[i],int(offset[i])))
            self.output[i]['yData'] = result.reshape(int(len(result)/size),size).mean(axis=0)

        return [out.copy() for out in self.output]

    def _initializeOutput(self):
        Nch = self.guzik.config()['Nch']
        n_S_ch = self.guzik.config()['n_S_ch']
        ch = self.guzik.config()["channels"]
        ch = ch.split(",")
        dt = self.guzik.config()['sampling_period_ns']*1e-9
        self.kwargs['Block Size'] = min(self.kwargs['Block Size'],n_S_ch)

        if self.guzik.config()['bits_16'] == True:
            data = np.zeros((Nch,int(self.kwargs['Block Size']/2+1)),dtype=np.int16)
        else:
            data = np.zeros((Nch,int(self.kwargs['Block Size']/2+1)),dtype=np.uint8)

        output = [self.outFmt.copy() for i in range(data.shape[0])]

        xData = np.fft.rfftfreq(int(self.kwargs['Block Size']),dt)

        for i in range(len(output)):
            output[i]['xData'] = xData
            output[i]["yData"] = data[i]
            output[i]["label"] = "Channel %s"%ch[i][-1]

        return output

class VoltageSpectrumCUDA(BlankMode):

    modeDomain = "Frequency"
    modeName = "Voltage Spectrum CUDA"
    plotType = "OneDimPlot"
    modeDimension = "1D"

    outFmt = {}
    outFmt['xData'] = None
    outFmt["yData"] = None
    outFmt["xLabel"] = "Frequency"
    outFmt["xUnit"] = "[Hz]"
    outFmt["yLabel"] = "Voltage spectrum"
    outFmt["yUnit"] = r"[V/$\sqrt{\rm Hz}$]"
    outFmt["label"] = None

    kwargs = {}
    kwargs["Block Size"] = 2048
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

        conv = self.guzik.config()['conv_resolution']
        offset = self.guzik.config()['conv_offset']
        size = int(self.kwargs['Block Size']/2+1)

        assert len(ch) == len(self.output), "Number of channels and outputs do not match."

        for i in range(len(self.output)):
            result = np.abs(digitizer_rFFT_cuda(data[i],int(self.kwargs['Block Size']),conv[i],int(offset[i])))
            self.output[i]['yData'] = result.reshape(int(len(result)/size),size).mean(axis=0)

        return [out.copy() for out in self.output]

    def _initializeOutput(self):
        Nch = self.guzik.config()['Nch']
        n_S_ch = self.guzik.config()['n_S_ch']
        ch = self.guzik.config()["channels"]
        ch = ch.split(",")
        dt = self.guzik.config()['sampling_period_ns']*1e-9
        self.kwargs['Block Size'] = min(self.kwargs['Block Size'],n_S_ch)

        if self.guzik.config()['bits_16'] == True:
            data = np.zeros((Nch,int(self.kwargs['Block Size']/2+1)),dtype=np.int16)
        else:
            data = np.zeros((Nch,int(self.kwargs['Block Size']/2+1)),dtype=np.uint8)

        output = [self.outFmt.copy() for i in range(data.shape[0])]

        xData = np.fft.rfftfreq(int(self.kwargs['Block Size']),dt)

        for i in range(len(output)):
            output[i]['xData'] = xData
            output[i]["yData"] = data[i]
            output[i]["label"] = "Channel %s"%ch[i][-1]

        return output


class PowerSpectrum(BlankMode):

    modeDomain = "Frequency"
    modeName = "Power Spectrum"
    plotType = "OneDimPlot"
    modeDimension = "1D"

    outFmt = {}
    outFmt['xData'] = None
    outFmt["yData"] = None
    outFmt["xLabel"] = "Frequency"
    outFmt["xUnit"] = "[Hz]"
    outFmt["yLabel"] = "Power spectrum"
    outFmt["yUnit"] = r"[V$^2$/Hz]"
    outFmt["label"] = None

    kwargs = {}
    kwargs["Block Size"] = 2048
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

        conv = self.guzik.config()['conv_resolution']
        offset = self.guzik.config()['conv_offset']
        size = int(self.kwargs['Block Size']/2+1)

        assert len(ch) == len(self.output), "Number of channels and outputs do not match."

        for i in range(len(self.output)):
            result = np.abs(digitizer_rFFT(data[i],int(self.kwargs['Block Size']),conv[i],int(offset[i])))**2
            self.output[i]['yData'] = result.reshape(int(len(result)/size),size).mean(axis=0)

        return [out.copy() for out in self.output]

    def _initializeOutput(self):
        Nch = self.guzik.config()['Nch']
        n_S_ch = self.guzik.config()['n_S_ch']
        ch = self.guzik.config()["channels"]
        ch = ch.split(",")
        dt = self.guzik.config()['sampling_period_ns']*1e-9
        self.kwargs['Block Size'] = min(self.kwargs['Block Size'],n_S_ch)

        if self.guzik.config()['bits_16'] == True:
            data = np.zeros((Nch,int(self.kwargs['Block Size']/2+1)),dtype=np.int16)
        else:
            data = np.zeros((Nch,int(self.kwargs['Block Size']/2+1)),dtype=np.uint8)

        output = [self.outFmt.copy() for i in range(data.shape[0])]

        xData = np.fft.rfftfreq(int(self.kwargs['Block Size']),dt)

        for i in range(len(output)):
            output[i]['xData'] = xData
            output[i]["yData"] = data[i]
            output[i]["label"] = "Channel %s"%ch[i][-1]

        return output

class PowerSpectrumCUDA(BlankMode):

    modeDomain = "Frequency"
    modeName = "Power Spectrum CUDA"
    plotType = "OneDimPlot"
    modeDimension = "1D"

    outFmt = {}
    outFmt['xData'] = None
    outFmt["yData"] = None
    outFmt["xLabel"] = "Frequency"
    outFmt["xUnit"] = "[Hz]"
    outFmt["yLabel"] = "Power spectrum"
    outFmt["yUnit"] = r"[V$^2$/Hz]"
    outFmt["label"] = None

    kwargs = {}
    kwargs["Block Size"] = 2048
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

        conv = self.guzik.config()['conv_resolution']
        offset = self.guzik.config()['conv_offset']
        size = int(self.kwargs['Block Size']/2+1)

        assert len(ch) == len(self.output), "Number of channels and outputs do not match."

        for i in range(len(self.output)):
            result = np.abs(digitizer_rFFT_cuda(data[i],int(self.kwargs['Block Size']),conv[i],int(offset[i])))**2
            self.output[i]['yData'] = result.reshape(int(len(result)/size),size).mean(axis=0)

        return [out.copy() for out in self.output]

    def _initializeOutput(self):
        Nch = self.guzik.config()['Nch']
        n_S_ch = self.guzik.config()['n_S_ch']
        ch = self.guzik.config()["channels"]
        ch = ch.split(",")
        dt = self.guzik.config()['sampling_period_ns']*1e-9
        self.kwargs['Block Size'] = min(self.kwargs['Block Size'],n_S_ch)

        if self.guzik.config()['bits_16'] == True:
            data = np.zeros((Nch,int(self.kwargs['Block Size']/2+1)),dtype=np.int16)
        else:
            data = np.zeros((Nch,int(self.kwargs['Block Size']/2+1)),dtype=np.uint8)

        output = [self.outFmt.copy() for i in range(data.shape[0])]

        xData = np.fft.rfftfreq(int(self.kwargs['Block Size']),dt)

        for i in range(len(output)):
            output[i]['xData'] = xData
            output[i]["yData"] = data[i]
            output[i]["label"] = "Channel %s"%ch[i][-1]

        return output

