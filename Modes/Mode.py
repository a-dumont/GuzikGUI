"""
Parent Mode class
"""
import numpy as np

class Mode:
	
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
			out["label"] = "Channel %s"%ch[i][-1]
			output[i] = out
			
		return output
		
	def getIndependantAxes(self):
		N = self.guzik.config()["n_S_ch"]
		dt = 1.0/self.guzik.config()["sampling_rate_GSs"]/1e9
		return np.linspace(0,N*dt,dt)
			
	def updateConfig(self, **newConfig):
		
		config = self.guzik.config()
		for key in newConfig.keys():
			assert key in config.keys(), "Key %s not in config"%keys
			config[key] = newConfig[key]
		self.gz.config(**config)
		
	def printConfig(self):
		
		config = self.guzik.config()
		for key in config.keys():
			print("%s: %s"%(key,str(),str(config[key])))
			
			
			
