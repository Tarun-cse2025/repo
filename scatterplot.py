import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("auto_mpg.csv")
plt.figure(figsize=(4,3))
plt.scatter(df['weight'], df['mpg'], color='green', edgecolors='black')
plt.title('Weight vsgi MPG')
plt.xlabel('weight')
plt.ylabel('MPG')
plt.show()