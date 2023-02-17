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
        self._config['n_S_ch'] = 1024
        return None

    def config(self):
        return self._config

    def __call__(self):
        out = np.zeros((self.config()['Nch'],self.config()['n_S_ch']),dtype=np.uint8)
        for i in range(out.shape[0]):
            out[i] = np.random.randint(0,255,self.config()['n_S_ch'],dtype=np.uint8)
        return out

class Mode(object):

    def __init__(self, guzik):

        self.modeName = "Blank"
        self.modeCategory = "None"
        self.modeDescription = "A blank mode used as a base."

        self.plotType = "1D plot"

        self.guzik = guzik

    def __repr__(self):
        return "<Mode object at %s>"%str(hex(id(self)))

    def __str__(self):
        return "Blank mode"

    def __call__(self):

        data = get(self.guzik)

        if self.guzik.config()["Nch"] == 1:
            data = np.array([data])

        output = [None for i in range(data.shape[0])]

        ch = self.guzik.config()["channels"]
        ch = ch.split(",")
        xData = self.getXData()

        for i in range(len(output)):
            out = {}
            out['xData'] = xData
            out["yData"] = data[i]
            out["xLabel"] = "Time"
            out["xUnit"] = "s"
            out["yLabel"] = "Voltage"
            out["yUnit"] = "V"
            out["label"] = "Channel %s"%ch[i][-1]
            output[i] = out

        return output

    def getXData(self):
        N = self.guzik.config()["n_S_ch"]
        dt = 1.0/self.guzik.config()["sampling_rate_GSs"]/1e9
        return np.linspace(0,N*dt,N)

    #def updateConfig(self, newConfig):

        #config = self.guzik.config()
        #for key in newConfig.keys():
        #    assert key in config.keys(), "Key %s not in config"%key
        #    config[key] = newConfig[key]
        #self.guzik.config(**config)

    def printConfig(self):

        config = self.guzik.config()
        for key in config.keys():
            print("%s: %s"%(key,str(config[key])))
