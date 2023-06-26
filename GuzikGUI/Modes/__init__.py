from GuzikGUI.Modes.Mode import BlankMode
from GuzikGUI.Modes.Mode import dummy_guzik

from GuzikGUI.Modes.TimeDomain import TimeSeries
from GuzikGUI.Modes.TimeDomain import OneDimHistogram
from GuzikGUI.Modes.TimeDomain import TwoDimHistogram

from GuzikGUI.Modes.FrequencyDomain import VoltageSpectrum
from GuzikGUI.Modes.FrequencyDomain import PowerSpectrum

try:
    from GuzikGUI.Modes.FrequencyDomain import VoltageSpectrumCUDA
    from GuzikGUI.Modes.FrequencyDomain import PowerSpectrumCUDA
    from GuzikGUI.Modes.FrequencyDomain import CrossPowerSpectrumCUDA
except:
    pass
