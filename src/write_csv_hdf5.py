import numpy
import pandas

df = pandas.DataFrame(numpy.random.randn(1000000,10))

df.to_csv('test.csv',mode='w')
df.to_hdf('test.h5','df',mode='w')
