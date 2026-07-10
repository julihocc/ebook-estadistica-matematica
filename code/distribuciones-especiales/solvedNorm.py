from scipy import stats

mu = 1500
sigma = 350
nd = stats.norm(mu, sigma)

def F(x):
    return nd.cdf(x)

#a
print(F(750))
##0.3471108697

#b
print(1-F(2000))
##0.0765637255098

def inverseF(x):
    return nd.ppf(x)
#c
print(inverseF(.90))
##1948.54304794
