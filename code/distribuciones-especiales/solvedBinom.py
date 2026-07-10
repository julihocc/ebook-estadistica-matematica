from scipy import stats

#7.2 N=50, p=15%
def f(x):
    return stats.binom(50,.15).pmf(x)
def F(x):
    return stats.binom(50,.15).cdf(x)
#(a) P(X<=10)
print(sum([f(x) for x in range(0,10+1)]))
##0.8800826828
print(F(10))
##0.8800826828
#(b) P(X>=5)
print(1-sum([f(x) for x in range(0,4+1)]))
##0.887894791945
print(1-F(4))
##0.887894791945
#(c) P(3<=X<=6)
print(sum([f(x) for x in range(3,6+1)]))
##0.3471108697
print(F(6)-F(2))
##0.3471108697
#(d) P(X=5)
print(f(5))
##0.3471108697
