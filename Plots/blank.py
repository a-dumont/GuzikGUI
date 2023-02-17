"""

"""
import matplotlib.pyplot as plt
import numpy as np

class BlankPlot(object):
    def __init__(self):
        fig, ax = plt.subplots()
        self.fig = fig
        self.axes = [ax]
        return None

    def initialOutput(self, output):
        fig = self.fig
        axes = self.axes

        assert type(output) == list, "Output must be a list."
        for i in output:
            assert type(i) == dict, "Output must be a list containing dictionnaries."

        N = len(output)
        xLabels = [None for i in range(N)]
        xUnits = [None for i in range(N)]
        yLabels = [None for i in range(N)]
        yUnits = [None for i in range(N)]
        labels = [None for i in range(N)]

        for i in range(N):
            try:
                xLabels[i] = output[i]['xLabel']
                xUnits[i] = output[i]['xUnit']
                yLabels[i] = output[i]['yLabel']
                yUnits[i] = output[i]['yUnit']
                labels[i] = output[i]['label']
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

        self.xLabel = xLabels[0]
        self.xUnit = xUnits[0]
        self.yLabel = yLabels[0]
        self.yUnit = yUnits[0]
        self.labels = labels


        for i in range(N):
            xData = output[i]['xData']
            yData = output[i]['yData']
            assert len(xData) == len(yData), "x and y have different lengths."
            axes[0].plot(xData,yData,label=labels[i])

        for ax in axes:
            ax.set_xlabel('%s %s'%(self.xLabel,self.xUnit))
            ax.set_ylabel('%s %s'%(self.yLabel,self.yUnit))
            ax.legend()

        return None
