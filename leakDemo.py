from pymodelica import compile_fmu
from pyfmi import load_fmu
import matplotlib.pyplot as plt
import numpy as np

fmu_name = compile_fmu('leakPipeline','leakPipeline.mo')
leakPipeline = load_fmu(fmu_name)
# leakPipeline.set('L',56.67)
opts = leakPipeline.simulate_options()
opts['ncp'] = 5000
res = leakPipeline.simulate(final_time=200,options=opts)
Q1 = res['Q[1]']
Q5 = res['Q[5]']
t = res['time']
r1 = 2.45e-5*np.random.randn(Q1.size)
r5 = 2.45e-5*np.random.randn(Q5.size)
plt.plot(t,Q1+r1,t,Q5+r5)
plt.ylim(0.0024,0.0037)
plt.grid(True)
plt.legend(['$Q_1(t)$','$Q_5(t)$'],loc='best')
plt.xlabel('Time (s)')
plt.ylabel('Flow rate (m$^3$/s)')
plt.show()