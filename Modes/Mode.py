"""
Parent Mode class
"""
import numpy as np
try:
        from pyHegel.commands import get
except:
        def get(guzik):
            """
            Dummy get function.
            """
            return guzik()

class dummy_guzik(object):
    """
    This class is used to test without needing access to the real guzik.
    """
    def __init__(self):
        """
        Implements parameters used by the module.
        """
        self._config = dict()
        self._config['Nch'] = 2
        self._config['channels'] = "CH1, CH3"
        self._config['bits_16'] = False
        self._config['sampling_rate_GSs'] = 32.0
        self._config['sampling_period_ns'] = 0.03125
        self._config['n_S_ch'] = 1024
        self._config['gain_dB'] = [12.3,22.1]
        self._config['conv_resolution'] = [1e-4,1e-4]
        self._config['conv_offset'] = [128.0,128.0]
        self._config['offset'] = [0.0,0.0]
        self._config['equalizer_en'] = True
        self._config['force_slower_sampling'] = False
        self._config['ext_ref'] = 'default'
        return None

    def config(self,**kwargs):
        """
        Mimics the behavior of the guzik_adp7104().config() method.
        """
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
                self._config['offset'] = kwargs['offset']
            except:
                pass
            try:
                self._config['equalizer_en'] = kwargs['equalizer_en']
            except:
                pass
            try:
                self._config['force_slower_sampling'] = kwargs['force_slower_sampling']
            except:
                pass
            try:
                self._config['ext_ref'] = kwargs['ext_ref']
            except:
                pass
            try:
                self._config['Nch'] = len(kwargs['channels'])
                channels = ["CH%i"%i for i in kwargs['channels']]
                self._config['channels'] = ', '.join(channels)
                self._config['conv_resolution'] = [1e-4 for i in range(self._config['Nch'])]
                self._config['conv_offset'] = [128.0 for i in range(self._config['Nch'])]
            except:
                pass

    def __call__(self):
        """
        Works with the custom get() that is used when pyHegel is not found.
        """
        out = np.zeros((self.config()['Nch'],self.config()['n_S_ch']),dtype=np.uint8)
        for i in range(out.shape[0]):
            out[i] = np.random.randint(0,256,self.config()['n_S_ch'],dtype=np.uint8)
        if self.config()['Nch'] == 1:
            out = out[0]
        return out

class BlankMode(object):
    """
    General Mode parameters and requirements.

    Required parameters:
        modeDomain,    str, Needed by the GUI to sort modes.
        modeName,      str, Needed by the GUI to display mode in menus.
        plotType,      str, Default plot class type. See Plots submodules for options.
        modeDimension, str, Needed by the GUI to give relevant plotting options.
        outFmt,       dict, Used to format the output.
        kwargs,       dict, Used to modify the behavior of __call__.
        output,       list, List of dictionaries using outFmt as a template.

    outFmt:
        'xData',  np.ndarray, x-axis data.
        'yData',  np.ndarray, y-axis data.
        'zData',  np.ndarray, z-axis data.  Used in 2D plots only.
        'xLabel',        str, x-axis label.
        'yLabel',        str, y-axis label.
        'zLabel',        str, z-axis label. Used in 2D plots only.
        'xUnit',         str, x-axis unit.
        'yUnit',         str, y-axis unit.
        'zUnit',         str, z-axis unit. Used in 2D plots only.
        'label',         str, Used to label the curve on the plot.

    kwargs:
        Must contain at most three keys and values. The values must be numeric 
        to be compatible with the GUI. This is a workaround to avoid having to 
        pass arguments to __call__.

    output:
        A list of outFmt style dictionaries. This is used to return multiple lines 
        at once. A simple usecase is to read and return the voltages on multiple 
        channels in a single call.

    All the above parameters need to be defined outside __init__ to be accessed by 
    the GUI without instancing. For outFmt and kwargs the values can be changed during 
    initialization but the keys should not be modified.
    """

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

    kwargs = {}
    kwargs["Not Used 1"] = 0
    kwargs["Not Used 2"] = 0
    kwargs["Not Used 3"] = 0

    def __init__(self, guzik):
        """
        Initializes the mode.
        Parameters:
            guzik: Instance of dummy_guzik or guzik_adp7104
        """
        self.guzik = guzik
        self.output = self._initializeOutput()
        return None

    def __repr__(self):
        return "<Mode object at %s>"%str(hex(id(self)))

    def __str__(self):
        return "Blank mode"

    def __call__(self):
        """
        This function is used to get and return new data.
        When outFmt is properly initialized this function should only update 
        yData or zData (1D or 2D). Be sure to return a copy of self.output to avoid 
        problems with the GUI's averaging or other operations.
        """
        kwargs = self.kwargs
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
        """
        Used to define the static values of outFmt and populate self.output 
        accordingly.
        """
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
