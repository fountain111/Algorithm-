import  numpy as np
from statsmodels.tsa.stattools import acf, pacf
from statsmodels.graphics.tsaplots import plot_acf
TimeSeries = [13, 8, 15, 4, 4, 12, 11, 7, 14, 12]

seq_list = []

lag = {}
mean = np.mean(TimeSeries)
denominator = 0
numerator = 0
#不够优雅，以后再改
for i in range(len(TimeSeries)):
    seq_list.append([TimeSeries[:-i],TimeSeries[i:]])
    denominator+=np.power((TimeSeries[i]-mean),2)

for value in seq_list:
    for v in list(zip(value[0],value[1])):
        #print(v) #
        numerator+= ((v[0]-mean)*(v[1]-mean))
    print(numerator/denominator)
    numerator = 0
    #print(numerator/denominator)

#print(denominator)



#print(seq_list)

print('acf',acf(TimeSeries))
plot_acf(TimeSeries,lags=1)
