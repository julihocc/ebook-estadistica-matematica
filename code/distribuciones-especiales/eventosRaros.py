from scipy import stats
#7.28
#a
N = 2000
p = 0.001
print(stats.binom(N,p).pmf(3))
##0.180537328032
print(stats.poisson(N*p).pmf(3))
##0.180447044315
#(b)
print(1-stats.binom(N,p).cdf(2))
##0.32332356124
print(1-stats.poisson(N*p).cdf(2))
##0.323323583817
