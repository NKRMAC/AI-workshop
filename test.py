import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 

# Create a dataframe with three columns filled with random numbers
data = np.random.rand(100, 3)
df = pd.DataFrame(data, columns=['Column1', 'Column2', 'Column3'])

df['sum'] = df['Column1'] + df['Column2'] + df['Column3']

plt.hist(df['sum'])
plt.show()