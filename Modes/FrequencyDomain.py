"""
Time Series measurement.
"""
import numpy as np
from .Mode import BlankMode
from SignalProcessing.fft import digitizer_FFT, digitizer_rFFT

try:
    from pyHegel.commands import get
except:
    def get(guzik):
        return guzik()

class FFT(BlankMode):

    modeDomain = "Frequency"
    modeName = "FFT"
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

