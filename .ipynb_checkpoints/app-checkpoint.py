import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns


names = ["crim", "zn", "indus", "chas", "nox", "rm", "age", "dis", "rad", "tax", "ptratio", "b", "lstat", "medv"]
df = pd.read_csv("housing.csv", )

df['RM'].hist(bins=20)
plt.xlabel("Average number of rooms")
plt.ylabel("Count")
plt.show()
