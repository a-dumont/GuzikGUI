"""

"""
import matplotlib.pyplot as plt
import numpy as np

from .blank import BlankPlot

class OneDimPlot(BlankPlot):

    plotDimension = "1D"
    plotName = 'Line plot'

    def __init__(self, fig=None, axes=None):
        super(OneDimPlot,self).__init__(fig,axes)

        return None

    def updatePlot(self, _input, rescale=True):
        fig = self.fig
        axes = self.axes

        metadata = self.checkInput(_input)
        self.checkMetadata(metadata)

        N = len(_input)
        if len(axes[0].lines) != N:
            self.initialOutput(_input)

        for i in range(N):
            axes[0].lines[i].set_data(_input[i]['xData'],_input[i]['yData'])

        if rescale == True:
            for ax in axes:
                ax.relim()
                ax.autoscale_view()

        fig.canvas.draw_idle()
        fig.canvas.flush_events()
        return None

class OneDimPlotAbs(BlankPlot):

    plotDimension = "1D"
    plotName = 'Complex amplitude plot'

    def __init__(self, fig=None, axes=None):
        super(OneDimPlotAbs,self).__init__(fig,axes)

        return None

    def updatePlot(self, _input, rescale=True):
        fig = self.fig
        axes = self.axes

        metadata = self.checkInput(_input)
        self.checkMetadata(metadata)

        N = len(_input)
        if len(axes[0].lines) != N:
            self.initialOutput(_input)

        for i in range(N):
            axes[0].lines[i].set_data(_input[i]['xData'],_input[i]['yData'])

        if rescale == True:
            for ax in axes:
                ax.relim()
                ax.autoscale_view()

        fig.canvas.draw_idle()
        fig.canvas.flush_events()
        return None
