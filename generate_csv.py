import pandas as pd
import numpy as np

np.random.seed(42)
n = 208

# Generate random data representing the constructs
data = {
    'Respondent_ID': range(1, n + 1),
    'Age': np.random.randint(18, 60, n),
    'Gender': np.random.choice([0, 1], n),
    'Ownership_Months': np.random.randint(1, 36, n),
    'Func1': np.random.randint(2, 6, n),
    'Func2': np.random.randint(2, 6, n),
    'Func3': np.random.randint(2, 6, n),
    'Usab1': np.random.randint(2, 6, n),
    'Usab2': np.random.randint(2, 6, n),
    'Usab3': np.random.randint(2, 6, n),
    'Price1': np.random.randint(2, 6, n),
    'Price2': np.random.randint(2, 6, n),
    'Price3': np.random.randint(2, 6, n),
    'Brand1': np.random.randint(3, 6, n),
    'Brand2': np.random.randint(3, 6, n),
    'Brand3': np.random.randint(3, 6, n),
    'Sat1': np.random.randint(2, 6, n),
    'Sat2': np.random.randint(2, 6, n),
    'Loyal1': np.random.randint(2, 6, n),
    'Loyal2': np.random.randint(2, 6, n),
}

df = pd.DataFrame(data)
df.to_csv('d:/Projects/Data_Science/gogoro_data.csv', index=False)
print("gogoro_data.csv created successfully with 208 rows.")
