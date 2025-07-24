import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("auto_mpg.csv")
plt.boxplot(df['mpg'], vert=True)
plt.title('MPG Box Plot')
plt.xlabel('MPG')
plt.show()

print("Min, Q1, Median, Q3, Max:")
print(df['mpg'].describe()[['min', '25%', '50%', '75%', 'max']])