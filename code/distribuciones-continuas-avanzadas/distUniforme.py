from scipy import stats
import numpy as np
import matplotlib.pyplot as plt

# Distribuci\'on uniforme continua en [a, b]
a, b = 0, 15
uniformDist = stats.uniform(loc=a, scale=b-a)

# P(X < 5)
print(uniformDist.cdf(5))
##0.3333333333333333

# Media y varianza
print(uniformDist.mean())   # 7.5
##7.5
print(uniformDist.var())    # 18.75
##18.75

# Simulaci\'on
np.random.seed(0)
muestras = np.random.uniform(a, b, size=10000)
print(f"Media muestral: {np.mean(muestras):.2f}")  # ~7.5
##Media muestral: 7.51
print(f"Var muestral: {np.var(muestras):.2f}")      # ~18.75
##Var muestral: 18.71

# Gr\'afica: densidad y CDF
fig, axes = plt.subplots(1, 2, figsize=(12, 4))
x = np.linspace(a-2, b+2, 200)

axes[0].plot(x, uniformDist.pdf(x), 'b-', lw=2)
axes[0].fill_between(x, uniformDist.pdf(x), where=(x>=a)&(x<=b), alpha=0.3)
axes[0].set_xlabel('x')
axes[0].set_ylabel('f(x)')
axes[0].set_title('Densidad U(0,15)')
axes[0].grid(True, alpha=0.3)

axes[1].plot(x, uniformDist.cdf(x), 'r-', lw=2)
axes[1].set_xlabel('x')
axes[1].set_ylabel('F(x)')
axes[1].set_title('CDF U(0,15)')
axes[1].grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig('pe/distUniforme.png', dpi=100, bbox_inches='tight')
plt.show()
