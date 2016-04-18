import numpy as np
import pandas as pd

prefix='../dataset/movies.csv'
users=pd.read_csv(prefix,names=["movieId","titles","genres"],header=None,index_col='movieId');

print users.head()
print "Dataset size: ", users.size
