"""
Time Series measurement.
"""
import numpy as np
from _Mode import Mode
from SignalProcessing.histograms import digitizer_histogram
from SignalProcessing.histograms import digitizer_histogram2D

class TimeSeries(Mode):
	
	def __init__(self,guzik):
		
		super().__init__(guzik)
		
		self.modeName = "Time series"
		self.modeCategory = "Time domain"
		self.modeDescription = "A mode for raw time domain measurements."
		
		self.plotType = "line"
		
	def __repr__(self):
		return "<TimeSeries object at %s>"%str(hex(id(self)))
		
	def __str__(self):
		return "Time series mode"
	
	def __call__(self):
		
		data = get(self.guzik)
		output = [None for i in range(data.shape[0])]
		ch = self.guzik.config()["channels"]
		ch = ch.split(",")
		
		assert len(ch) == len(output), "Number of channels and outputs do not match."
		
		for i in range(len(out)):
			out = {}
			out["data"] = data[i]
			out["xLabel"] = "Time"
			out["xUnit"] = "[s]"
			out["yLabel"] = "Voltage"
			out["yUnit"] = "[V]"
			out["label"] = "Channel %i"%ch[i]
			output[i] = out
			
		return output
		
class OneDimHistogram(Mode):
	
	def __init__(self,guzik):
		
		super().__init__(guzik)
		
		self.modeName = "1D Histogram"
		self.modeCategory = "Time domain"
		self.modeDescription = "A mode for 1D time domain histograms."
		
		self.plotType = "line"
		
		if self.guzig.config()["bits_16"] is True:
			self.nbits = 16
			self.nbits_out = 10
		else:
			self.nbits = 8
			self.nbits_out = 8
		
	def __repr__(self):
		return "<1DHistogram object at %s>"%str(hex(id(self)))
		
	def __str__(self):
		return "1D Histogram mode"
	
	def __call__(self):
		
		data = get(self.guzik)
		output = [None for i in range(data.shape[0])]
		ch = self.guzik.config()["channels"]
		ch = ch.split(",")
		
		assert len(ch) == len(output), "Number of channels and outputs do not match."
		
		for i in range(len(out)):
			out = {}
			out["data"] = digitizer_histogram(data[i],self.nbits)[0:1<<self.nbits_out]
			out["xLabel"] = "Bin"
			out["xUnit"] = ""
			out["yLabel"] = "Count"
			out["yUnit"] = ""
			out["label"] = "Channel %i"%ch[i]
			output[i] = out
			
		return output
			
	def getIndependantAxes(self):
		return np.linspace(0,1<<self.nbits_out,1)
		
class TwoDimHistogram(Mode):
	
	def __init__(self,guzik):
		
		super().__init__(guzik)
		
		self.modeName = "2D Histogram"
		self.modeCategory = "Time domain"
		self.modeDescription = "A mode for 2D time domain histograms."
		
		self.plotType = "colormap"
		
		if self.guzig.config()["bits_16"] is True:
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
		
		data = get(self.guzik)
		output = [None]
		ch = self.guzik.config()["channels"]
		ch = ch.split(",")
		
		assert len(ch) == 2, "Number of channels and outputs do not match."
		
		out = {}
		out["data"] = digitizer_histogram2D(data[0],data[1],self.nbits)[0:1<<self.nbits_out,0:1:<<self.nbits_out]
		out["xLabel"] = "Channel %s"%ch[0]
		out["xUnit"] = "[Bin]"
		out["yLabel"] = "Channel %s"%ch[1]
		out["yUnit"] = "[Bin]"
		out["label"] = ""
		output[0] = out
			
		return output
			
	def getIndependantAxes(self):
		x = np.linspace(0,1<<self.nbits_out,1)
		return x, x