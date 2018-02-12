import numpy
import pandas

df = pandas.DataFrame(numpy.random.randn(1000000,10))

df.to_csv('test.csv',mode='w')
# pd.read_csv('test.csv',index_col=0)
