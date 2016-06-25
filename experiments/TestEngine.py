from service.BaseEngine import BaseEngine
from utils.auto_load import AutoLoad
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from perioddetection import autoperiod
loader = AutoLoad()
engine = loader.auto_load_engine_default(method='SHESD')
dat = pd.read_csv('../data/vc_1.json_remake',index_col=0,parse_dates=True)
engine.longterm = True;
engine.piecewise_median_period = 4;
engine.max_anoms = 1/200.0
engine.fit(data=dat.points)
engine.custom_period = np.min(autoperiod.period_detect(engine.data,segment_method = "slidingwindowsegment"))
print engine.custom_period
engine.fit_predict(data=dat.points)
engine.plot()
plt.show()
