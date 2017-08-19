import re
import csv
import pandas as pd
import math

df = pd.read_csv('uevent.csv')
df = df['页面']
l = [i for i in df.values]

