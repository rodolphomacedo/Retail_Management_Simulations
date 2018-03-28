import numpy as np
from scipy.stats import gamma
import matplotlib.pyplot as plt

fig, ax = plt.subplots()

alpha = 0.05
beta = 0.4

days = np.linspace(1,365,365)
hours = np.linspace(1,365*24,365*24)
sales = gamma.rvs(alpha, scale=beta, size=len(days))
sales = gamma.rvs(alpha, scale=beta, size=len(hours))

#ax.plot( days, np.around(sales), '-o', ms=5, lw=1, alpha=0.7, mfc='red')
ax.plot( hours, np.around(sales), '-o', ms=5, lw=1, alpha=0.7, mfc='red')
plt.show()
