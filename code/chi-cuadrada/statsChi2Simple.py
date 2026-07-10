from scipy.stats import chi2
import numpy as np
import matplotlib.pyplot as plt
fig, ax = plt.subplots(1, 1)

df = 55

x = np.linspace(chi2.ppf(0.01, df),
chi2.ppf(0.99, df), 100)
ax.plot(x, chi2.pdf(x, df),'r-',
lw=5, alpha=0.6, label='chi2 pdf')
