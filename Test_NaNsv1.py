#!/usr/bin/python3

# Import the relevant libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import plotly.offline as py
# py.init_notebook_mode(connected=True)
import plotly.graph_objs as go
import plotly.tools as tls
import seaborn as sns
import warnings
import csv
warnings.filterwarnings('ignore')

# %matplotlib inline

# The encoding addition overcomes, UnicodeDecodeError: 'utf-8' codec can't decode byte 0xf4 in position 2: invalid continuation byte
# Read Files
Test_DF = pd.read_csv('/home/williamsrka/Programming/Test_NaNs.csv', sep=',')

Test_DF.shape

Test_DF.describe

Test_DF.groupby("Type").describe()