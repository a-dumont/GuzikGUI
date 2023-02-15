"""
Time Series measurement.
"""
import numpy as np
from Mode import Mode

class TimeSeries(Mode):
	
	def __init__(self,guzik):
		
		super().__init__(guzik)
		
		self.modeName = "Time series"
		self.modeCategory = "Time domain"
		self.modeDescription = "A mode for raw time domain measurements."
		
		self.plotType = "1D"
		
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
			out["xUnit"] = "s"
			out["yLabel"] = "Voltage"
			out["yUnit"] = "V"
			out["label"] = "Channel %i"%ch[i]
			output[i] = out
			
		return output