"""
Parent Mode class
"""
import numpy as np
try:
        from pyHegel.commands import get
except:
        def get(guzik):
            return guzik()

class dummy_guzik(object):
    def __init__(self):
        self._config = dict()
        self._config['Nch'] = 2
        self._config['channels'] = "CH1, CH3"
        self._config['bits_16'] = False
        self._config['sampling_rate_GSs'] = 32
        self._config['sampling_period_ns'] = 0.03125
        self._config['n_S_ch'] = 1024
        self._config['gain_dB'] = [12.3,22.1]
        return None

    def config(self,**kwargs):
        if len(kwargs) == 0:
            return self._config
        else:
            try:
                self._config['n_S_ch'] = kwargs['n_S_ch']
            except:
                pass
            try:
                self._config['bits_16'] = kwargs['bits_16']
            except:
                pass
            try:
                self._config['gain_dB'] = kwargs['gain_dB']
            except:
                pass
            try:
                self._config['Nch'] = len(kwargs['channels'])
                channels = ["CH%i"%i for i in kwargs['channels']]
                self._config['channels'] = ', '.join(channels)
            except:
                pass

    def __call__(self):
        out = np.zeros((self.config()['Nch'],self.config()['n_S_ch']),dtype=np.uint8)
        for i in range(out.shape[0]):
            out[i] = np.random.randint(0,256,self.config()['n_S_ch'],dtype=np.uint8)
        return out

class BlankMode(object):

    modeDomain = "Time"
    modeName = "Blank"
    plotType = "BlankPlot"
    modeDimension = "1D"

    outFmt = {}
    outFmt['xData'] = None
    outFmt["yData"] = None
    outFmt["xLabel"] = "Time"
    outFmt["xUnit"] = "[s]"
    outFmt["yLabel"] = "Voltage"
    outFmt["yUnit"] = "[Bin]"
    outFmt["label"] = None

    def __init__(self, guzik):
        self.guzik = guzik
        self.output = self._initializeOutput()
        return None

    def __repr__(self):
        return "<Mode object at %s>"%str(hex(id(self)))

    def __str__(self):
        return "Blank mode"

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
