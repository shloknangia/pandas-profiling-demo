import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt

# Import pandas profiling library
import ydata_profiling as pp


# Import Iris Dataset
df_iris = pd.read_csv('./Iris.csv')
df_iris.info()


# Geneate  Report 
pp.ProfileReport(df_iris, title="Pandas Profiling Report").to_file("report.html")


