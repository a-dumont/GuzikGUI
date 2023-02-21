"""

"""
import matplotlib.pyplot as plt
import numpy as np

class BlankPlot(object):
    def __init__(self, fig=None, axes=None):
        plt.ion()
        if fig == None and axes == None:
            fig, ax = plt.subplots()
            self.fig = fig
            self.axes = [ax]
        else:
            self.fig = fig
            self.axes = axes

        self.xLabel = None
        self.xUnit = None
        self.yLabel = None
        self.yUnit = None
        self.labels = None

        return None

    def checkInput(self, _input):
        assert type(_input) == list, "Input must be a list."
        for i in _input:
            assert type(i) == dict, "Input must be a list containing dictionnaries."

        N = len(_input)
        xLabels = [None for i in range(N)]
        xUnits = [None for i in range(N)]
        yLabels = [None for i in range(N)]
        yUnits = [None for i in range(N)]
        labels = [None for i in range(N)]

        for i in range(N):
            try:
                xLabels[i] = _input[i]['xLabel']
                xUnits[i] = _input[i]['xUnit']
                yLabels[i] = _input[i]['yLabel']
                yUnits[i] = _input[i]['yUnit']
                labels[i] = _input[i]['label']
            except KeyError:
                raise RuntimeError("Output is missing default keys. See Modes documentation.")

        xLabels = np.unique(np.array([xLabels])).tolist()
        xUnits = np.unique(np.array([xUnits])).tolist()
        yLabels =np.unique(np.array([yLabels])).tolist()
        yUnits = np.unique(np.array([yUnits])).tolist()

        assert len(xLabels) == 1, "Multiple xLabels defined."
        assert len(xUnits) == 1, "Multiple xUnits defined."
        assert len(yLabels) == 1, "Multiple yLabels defined."
        assert len(yUnits) == 1, "Multiple yUnits defined."

        return xLabels[0], xUnits[0], yLabels[0], yUnits[0], labels

    def checkMetadata(self, metadata):
        assert metadata[0] == self.xLabel, "xLabel has changed."
        assert metadata[1] == self.xUnit, "xUnit has changed."
        assert metadata[2] == self.yLabel, "yLabel has changed."
        assert metadata[3] == self.yUnit, "yUnit has changed."
        return None

    def initialOutput(self, _input):
        fig = self.fig
        axes = self.axes

        for ax in axes:
            ax.clear()

        N = len(_input)
        metadata = self.checkInput(_input)

        self.xLabel = metadata[0]
        self.xUnit = metadata[1]
        self.yLabel = metadata[2]
        self.yUnit = metadata[3]
        self.labels = metadata[4]

        for i in range(N):
            xData = _input[i]['xData']
            yData = _input[i]['yData']
            #assert len(xData) == len(yData), "x and y have different lengths."
            axes[0].plot(xData,yData,label=self.labels[i])

        for ax in axes:
            ax.set_xlabel('%s %s'%(self.xLabel,self.xUnit))
            ax.set_ylabel('%s %s'%(self.yLabel,self.yUnit))
            ax.legend(ncols=N,loc="upper center")

        return None

    def updatePlot(self, _input, rescale=True):
        fig = self.fig
        axes = self.axes

        metadata = self.checkInput(_input)
        self.checkMetadata(metadata)

        N = len(_input)

        for i in range(N):
            axes[0].lines[i].set_data(_input[i]['xData'],_input[i]['yData'])

        if rescale == True:
            for ax in axes:
                ax.relim()
                ax.autoscale_view()

        fig.canvas.draw_idle()
        fig.canvas.flush_events()
        return None
